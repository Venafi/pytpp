from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import InvalidResultCode
from pytpp.attributes.policy import PolicyAttributes
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Config, Identity


@feature('Folder')
class Folder(FeatureBase):
    def __init__(self, api):
        super().__init__(api)

    def apply_workflow(self, folder: 'Union[Config.Object, str]', workflow: 'Union[Config.Object, str]'):
        """
        Applies a workflow to a folder and all of its subordinate objects. However, a subordinate folder
        may block the workflow.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            workflow: :ref:`config_object` or :ref:`dn` of the workflow object.
        """
        folder_dn = self._get_dn(folder)
        workflow_dn = self._get_dn(workflow)
        result = self._api.websdk.Config.AddValue.post(
            object_dn=folder_dn,
            attribute_name=PolicyAttributes.workflow,
            value=workflow_dn
        )

        result.assert_valid_response()

    def block_workflow(self, folder: 'Union[Config.Object, str]', workflow: 'Union[Config.Object, str]'):
        """
        Blocks a workflow on a folder and all of its subordinate objects. This prevents any parent folders from
        enforcing a workflow on this folder and its subordinate objects.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            workflow: :ref:`config_object` or :ref:`dn` of the workflow object.
        """
        folder_dn = self._get_dn(folder)
        workflow_dn = self._get_dn(workflow)
        result = self._api.websdk.Config.AddValue.post(
            object_dn=folder_dn,
            attribute_name=PolicyAttributes.workflow_block,
            value=workflow_dn
        )

        result.assert_valid_response()

    def clear_policy(self, folder: 'Union[Config.Object, str]', class_name: str, attributes: Union[dict, List[str]]):
        """
        If ``attributes`` are not provided, clears the policy attribute name along with all of its values
        on a folder. If ``attributes`` are provided, then only the corresponding policy attribute values
        will be cleared. No error is thrown if the attribute value doesn't exist to begin with. If the
        same attribute name is defined in any ancestor folder, then this folder will inherit that setting.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            class_name: TPP Class Name for the attributes being locked.
            attributes: Two types are supported:

                * ``list`` of attribute names to be cleared entirely.
                * ``dict`` whose keys are attribute names and whose values are the values to be cleared
                  from the attribute. If the attribute is left empty it is cleared.
        """
        folder_dn = self._get_dn(folder)
        if isinstance(attributes, list):
            for attribute_name in attributes:
                result = self._api.websdk.Config.ClearPolicyAttribute.post(
                    object_dn=folder_dn,
                    attribute_name=attribute_name,
                    class_name=str(class_name)
                ).result

                if result.code != 1:
                    raise InvalidResultCode(code=result.code, code_description=result.config_result)

        elif isinstance(attributes, dict):
            for name, values in attributes.items():
                if not isinstance(values, list):
                    values = [values]

                for value in values:
                    result = self._api.websdk.Config.RemovePolicyValue.post(
                        object_dn=folder_dn,
                        class_name=str(class_name),
                        attribute_name=name,
                        value=value
                    ).result

                    if result.code != 1:
                        raise InvalidResultCode(code=result.code, code_description=result.config_result)
        else:
            raise TypeError(f'Expected attributes to be of type List[str] or Dict, but got {type(attributes)} instead.')

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None, log_server: 'Union[Config.Object, str]' = None,
               engines: 'List[Union[Config.Object, str]]' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the folder.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            description: Description of the policy folder.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` of the contacts.
            log_server: :ref:`config_object` or name of the log server.
            engines: List of :ref:`config_object` or names of the processing engines for this folder.
            attributes: Attributes pertaining to the folder itself and NOT any of the policyable options.
                In order to set engines on this folder, use :meth:`set_engines`. In order to set policyable
                options on the folder, use :meth:`write_policy`.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the folder object.
        """
        folder_attrs = {
            PolicyAttributes.description: description,
            PolicyAttributes.contact: [self._get_prefixed_universal(c) for c in contacts] if contacts else None,
        }
        if attributes:
            folder_attrs.update(attributes)

        folder = self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=PolicyAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )
        if log_server:
            self._api.websdk.Config.WritePolicy.post(
                object_dn=folder.dn,
                class_name=PolicyAttributes.__config_class__,
                attribute_name=PolicyAttributes.log_view_server,
                values=[self._get_dn(log_server, parent_dn=r'\VED\Logging')]
            )
        if engines:
            self.set_engines(folder=folder, engines=engines, append_engines=True)
        return folder

    def delete(self, folder: 'Union[Config.Object, str]', recursive: bool = True, delete_owners_from_secrets: bool = True, concurrency: int = 1):
        """
        Deletes the folder. The folder is, by default, deleted recursively. All deleted objects will also be removed from their
        secret associations. If the secret association is then orphaned, then it is deleted.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            recursive: If ``True``, delete all objects recursively.
            delete_owners_from_secrets: If ``True``, the owners will be removed from the associated secrets.
            concurrency: If greater than one a thread pool of this size will be used to delete the owner from the secret store association. If ``delete_owners_from_secrets`` is ``False`` then this has no effect.
        """
        folder_dn = self._get_dn(folder)
        response = self._api.websdk.Config.Enumerate.post(object_dn=folder_dn, recursive=recursive)
        result = response.result
        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)
        all_child_objects = response.objects
        if delete_owners_from_secrets:
            # Must delete all of the secrets first.
            with ThreadPoolExecutor(max_workers=concurrency) as pool:
                pool.map(self._secret_store_delete, all_child_objects)
            self._secret_store_delete(object_dn=folder_dn)
        self._config_delete(object_dn=folder_dn, recursive=recursive)

    def delete_engines(self, folder: 'Union[Config.Object, str]'):
        """
        Deletes all processing engines from the folder.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
        """
        folder_guid = self._get_guid(folder)
        return self._api.websdk.ProcessingEngines.Folder.Guid(folder_guid).delete()

    def get(self, folder_dn: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            folder_dn: :ref:`dn` of the folder.
            raise_error_if_not_exists: Raise an exception if the object :ref:`dn` does not exist.

        Returns:
            :ref:`config_object` of the folder object.
        """
        return self._get_config_object(
            object_dn=folder_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def get_engines(self, folder: 'Union[Config.Object, str]'):
        """
        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.

        Returns:
            List of all :class:`~.dataclasses.processing_engines.Engine` on the folder.
        """
        folder_guid = self._get_guid(folder)
        return self._api.websdk.ProcessingEngines.Folder.Guid(folder_guid).get().engines

    def search(self, object_name_pattern: str = '*', object_types: List[str] = None, recursive: bool = True,
               starting_dn: str = None):
        """
        Searches for an object with the given object name pattern. The pattern is a regular expression. An object type
        can be supplied to specify the TPP object type, such as 'X509 Certificate'. If a starting :ref:`dn` is given without
        an object type, a search will be performed from the starting DN. This can improve the efficiency of this method.
        However, if both a starting DN and object type is provided, due to limitations of the WebSDK API, a search will
        be performed against the object type first, and then filtered by matches to the starting DN.

        Args:
            object_name_pattern: An expression for filtering DN matches.
            object_types: List of TPP Object Types (also called a Config Classes)
            recursive: Search sub-folders when True
            starting_dn: DN of the folder to begin search

        Returns:
            A list of :ref:`config_object` of the objects found.
        """
        if object_types:
            objects = self._api.websdk.Config.FindObjectsOfClass.post(
                classes=object_types,
                pattern=object_name_pattern,
                object_dn=starting_dn,
                recursive=recursive
            ).objects
        elif starting_dn:
            objects = self._api.websdk.Config.Enumerate.post(
                object_dn=starting_dn,
                pattern=object_name_pattern,
                recursive=recursive
            ).objects
        else:
            objects = self._api.websdk.Config.EnumerateAll.post(
                pattern=object_name_pattern
            ).objects

        return objects

    def set_engines(self, folder: 'Union[Config.Object, str]', engines: 'List[Union[Config.Object, str]]',
                    append_engines: bool = False):
        """
        Sets ``engines`` as processing engines for the folder.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            engines: List of engine :ref:`config_object` or engine names listed in TPP.
            append_engines: If ``True``, append ``engines`` to the current list on the folder. Otherwise
                overwrite the current setting.
        """
        folder_guid = self._get_guid(folder)
        engine_guids = [self._get_guid(e, parent_dn=r'\VED\Engines') for e in engines]
        if append_engines:
            current_engines = self._api.websdk.ProcessingEngines.Folder.Guid(folder_guid).get().engines
            engine_guids.extend([engine.engine_guid for engine in current_engines])
        result = self._api.websdk.ProcessingEngines.Folder.Guid(folder_guid).put(engine_guids=engine_guids)
        result.assert_valid_response()

    def read_policy(self, folder: 'Union[Config.Object, str]', class_name: str, attribute_name: str):
        """
        Reads policy settings for the given folder, class name, and attribute name.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            class_name: TPP Class Name for the attributes being locked.
            attribute_name: The attribute name.

        Returns:
            Tuple[List[str], bool]: A tuple of

                * List of values
                * Locked boolean
        """
        folder_dn = self._get_dn(folder)
        resp = self._api.websdk.Config.ReadPolicy.post(
            object_dn=folder_dn,
            class_name=str(class_name),
            attribute_name=attribute_name
        )

        result = resp.result
        if result.code != 1:
            InvalidResultCode(code=result.code, code_description=result.config_result).log()

        return resp.values, resp.locked

    def remove_workflow(self, folder: 'Union[Config.Object, str]', workflow: 'Union[Config.Object, str]'):
        """
        Removes an applied workflow from a folder.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            workflow: :ref:`config_object` or :ref:`dn` of the workflow object.
        """
        folder_dn = self._get_dn(folder)
        workflow_dn = self._get_dn(workflow)
        result = self._api.websdk.Config.RemoveDnValue.post(
            object_dn=folder_dn,
            attribute_name=PolicyAttributes.workflow,
            value=workflow_dn
        )

        result.assert_valid_response()

    def remove_blocked_workflow(self, folder: 'Union[Config.Object, str]', workflow: 'Union[Config.Object, str]'):
        """
        Removes a blocked workflow from a folder.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            workflow: :ref:`config_object` or :ref:`dn` of the workflow object.
        """
        folder_dn = self._get_dn(folder)
        workflow_dn = self._get_dn(workflow)
        result = self._api.websdk.Config.RemoveDnValue.post(
            object_dn=folder_dn,
            attribute_name=PolicyAttributes.workflow_block,
            value=workflow_dn
        )

        result.assert_valid_response()

    def write_policy(self, folder: 'Union[Config.Object, str]', class_name: str, attributes: dict, locked: bool):
        """
        Writes policy settings on a folder. In order to set engines on this folder, use :meth:`set_engines`.
        In order to set custom field policies, use :meth:`pytpp.features.custom_fields.CustomField.write_policy`.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            class_name: TPP Class Name for the attributes being locked.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
            locked: Enforces the policy on all subordinate folders and objects.
        """
        folder_dn = self._get_dn(folder)
        for name, values in attributes.items():
            if not isinstance(values, list):
                values = [values]

            result = self._api.websdk.Config.WritePolicy.post(
                object_dn=folder_dn,
                class_name=str(class_name),
                attribute_name=name,
                values=values,
                locked=locked
            ).result

            if result.code != 1:
                InvalidResultCode(code=result.code, code_description=result.config_result).log()

    def update_policy(self, folder: 'Union[Config.Object, str]', class_name: str, attributes: dict, locked: bool):
        """
        Updates policy configurations on a folder.

        Args:
            folder: :ref:`config_object` or :ref:`dn` of the folder.
            class_name: TPP Class Name for the attributes being locked.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
            locked: Enforces the policy on all subordinate folders and objects.
        """
        folder_dn = self._get_dn(folder)
        for name, value in attributes.items():
            result = self._api.websdk.Config.AddPolicyValue.post(
                object_dn=folder_dn,
                class_name=str(class_name),
                attribute_name=name,
                value=value,
                locked=locked,
            ).result

            if result.code != 1:
                raise InvalidResultCode(code=result.code, code_description=result.config_result)
