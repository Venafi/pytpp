from dataclasses import dataclass
from typing import List, Union
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import InvalidResultCode, InvalidFormat
from pytpp.tools.vtypes import Config


@dataclass
class AttributeValue:
    values: List[str]
    locked: bool


@feature('Objects')
class Objects(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def clear(self, obj: 'Union[Config.Object, str]', attributes: Union[dict, List[str]]):
        """
        Clears attributes from an object.
        
        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            attributes: Two types are supported:

                * ``list`` of attribute names to be cleared entirely.
                * ``dict`` whose keys are attribute names and whose values are the values to be cleared
                  from the attribute. If the attribute is left empty it is cleared.
        """
        obj_dn = self._get_dn(obj)
        if isinstance(attributes, list):
            for attribute_name in attributes:
                result = self._api.websdk.Config.ClearAttribute.post(
                    object_dn=obj_dn,
                    attribute_name=attribute_name
                ).result

                if result.code != 1:
                    raise InvalidResultCode(code=result.code, code_description=result.config_result)

        elif isinstance(attributes, dict):
            for name, values in attributes.items():
                if not isinstance(values, list):
                    values = [values]

                for value in values:
                    result = self._api.websdk.Config.RemoveDnValue.post(
                        object_dn=obj_dn,
                        attribute_name=name,
                        value=value
                    ).result

                    if result.code != 1:
                        raise InvalidResultCode(code=result.code, code_description=result.config_result)
        else:
            raise TypeError(f'Expected attributes to be of type "list" or "dict", but got {type(attributes)} instead.')

    def exists(self, object_dn: str = None):
        """
        Args:
            object_dn: The :ref:`dn` of the object.

        Returns:
           bool: ``True`` if ``object_dn`` exist, else ``False``.
        """
        dn = self._get_dn(obj=object_dn)
        result = self._api.websdk.Config.IsValid.post(object_dn=dn)
        return result.is_valid_response() and result.result.code == 1

    def find_policy(self, obj: 'Union[Config.Object, str]', class_name: str, attribute_name: str):
        """
        Find the folder that defines the policy attribute of the ``class_name`` on a given object.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            class_name: TPP class name of the object.
            attribute_name: Name of the attribute.

        Returns:
            Tuple[str, List[str], bool]: A ``tuple`` of

                * A :ref:`dn` of the folder implementing the policy.
                * A list of attribute values.
                * ``True`` if the policy value is locked, else ``False``.
        """
        obj_dn = self._get_dn(obj)
        resp = self._api.websdk.Config.FindPolicy.post(
            object_dn=obj_dn,
            class_name=str(class_name),
            attribute_name=attribute_name
        )

        result = resp.result
        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

        class Policy:
            policy_dn = resp.policy_dn
            values = resp.values
            locked = resp.locked

        return Policy()

    def get(self, object_dn: str = None, object_guid: str = None, raise_error_if_not_exists: bool = True):
        """
        One of ``object_dn`` or ``object_guid`` is required.

        Args:
            object_dn: :ref:`dn` of the object.
            object_guid: GUID of the object.
            raise_error_if_not_exists: If ``True`` raise an exception if the obejct doesn't exist.

        Returns:
            :ref:`config_object` of the object.
        """
        return self._get_config_object(
            object_dn=object_dn,
            object_guid=object_guid,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def read(self, obj: 'Union[Config.Object, str]', attribute_name: str, include_policy_values: bool = False, timeout: int = 10):
        """
        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            attribute_name: The attribute name.
            include_policy_values: If ``True``, the effective value(s) are returned.
                Otherwise only values explicitly assigned to the object are returned.
            timeout: Read timeout in seconds.

        Returns:
            An ``AttributeValue`` object with these properties

            * **values** *(List[str])* - List of attribute values.
            * **locked** *(bool)* - ``True`` if the value is locked by policy.
        """
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                result, attr = self._read(
                    obj=obj,
                    attribute_name=attribute_name,
                    include_policy_values=include_policy_values
                )
                if result.code != 1:
                    continue
                if attr and attr.values:
                    return attr

        obj_dn = self._get_dn(obj)
        InvalidResultCode(code=result.code, code_description=result.config_result).log()
        raise TimeoutError(f'Could not read {attribute_name} on {obj_dn} because it did not exist '
                           f'after {timeout} seconds.')

    def read_all(self, obj: 'Union[Config.Object, str]'):
        """
        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.

        Returns:
            List of :class:`~.dataclasses.config.NameValues` where the

            * name is the attribute name.
            * values is the list of attribute values.
        """
        obj_dn = self._get_dn(obj)
        resp = self._api.websdk.Config.ReadAll.post(object_dn=obj_dn)

        result = resp.result
        if result.code != 1:
            InvalidResultCode(code=result.code, code_description=result.config_result).log()

        return resp.name_values

    def rename(self, obj: 'Union[Config.Object, str]', new_object_dn: str):
        """
        .. note::
            This method can be used to rename objects and move their location.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            new_object_dn: :ref:`dn` of the new object.
        """
        obj_dn = self._get_dn(obj)
        if not new_object_dn.startswith('\\VED'):
            raise InvalidFormat(f'"{new_object_dn}" must be an absolute path starting from \\VED.')

        response = self._api.websdk.Config.RenameObject.post(object_dn=obj_dn, new_object_dn=new_object_dn)
        result = response.result

        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

        return self.get(object_dn=new_object_dn, raise_error_if_not_exists=True)

    def update(self, obj: 'Union[Config.Object, str]', attributes: dict):
        """
        Updates attributes on an object. If the attribute is locked TPP will simply ignore the request.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
        """
        obj_dn = self._get_dn(obj)
        for name, value in attributes.items():
            result = self._api.websdk.Config.AddValue.post(
                object_dn=obj_dn,
                attribute_name=name,
                value=value,
            ).result

            if result.code != 1:
                raise InvalidResultCode(code=result.code, code_description=result.config_result)

    def wait_for(self, obj: 'Union[Config.Object, str]', attribute_name: str, attribute_value: str, include_policy_values: bool = False,
                 timeout: int = 10):
        """
        Waits for the ``attribute_name`` to have the ``attribute_value`` on the object within the timeout period. A
        ``TimeoutError`` is raised if the ``attribute_name`` does not have the ``attribute_value``.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            attribute_name: The name of the attribute.
            attribute_value: The expected value to the ``attribute_name``.
            include_policy_values: If ``True``, the effective value(s) are returned.
                Otherwise only values explicitly assigned to the object  are returned.
            timeout: Timeout period in seconds.

        Returns:
            An ``AttributeValue`` object with these properties

            * **values** *(List[str])* - List of attribute values.
            * **locked** *(bool)* - ``True`` if the value is locked by policy.
        """
        obj_dn = self._get_dn(obj)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                result, attr = self._read(
                    obj=obj_dn,
                    attribute_name=attribute_name,
                    include_policy_values=include_policy_values
                )
                if result.code != 1:
                    continue
                if attr and any([True for value in attr.values if str(value).lower() == attribute_value.lower()]):
                    return attr

        InvalidResultCode(code=result.code, code_description=result.config_result).log()
        raise TimeoutError(
            f'{attribute_name} on "{obj_dn}" did not return {attribute_value} in {timeout} seconds. '
            f'Got {attr.values} instead.'
        )

    def write(self, obj: 'Union[Config.Object, str]', attributes: dict):
        """
        Writes new attributes on an object. If the attribute is locked TPP will simply ignore the request.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
        """
        obj_dn = self._get_dn(obj)
        attributes = {k: ([v] if not isinstance(v, list) else v) for k, v in attributes.items()}

        result = self._api.websdk.Config.Write.post(
            object_dn=obj_dn,
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        ).result

        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

    def _read(self, obj: 'Union[Config.Object, str]', attribute_name: str, include_policy_values: bool):
        obj_dn = self._get_dn(obj)
        if include_policy_values is True:
            resp = self._api.websdk.Config.ReadEffectivePolicy.post(
                object_dn=obj_dn,
                attribute_name=attribute_name
            )
            return resp.result, AttributeValue(values=resp.values, locked=resp.locked)
        else:
            resp = self._api.websdk.Config.Read.post(
                object_dn=obj_dn,
                attribute_name=attribute_name
            )
            return resp.result, AttributeValue(values=resp.values, locked=False)
