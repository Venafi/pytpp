from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import InvalidResultCode
from pytpp.properties.config import ClientGroupsAttributeValues
from pytpp.attributes.client_group import ClientGroupAttributes
from typing import Union, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Config


class _ClientGroupBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api)

        self._group_base_dn = r'\VED\Clients\Groups'
        self._work_base_dn = r'\VED\Clients\Work'

    def assign_work(self, group: 'Union[Config.Object, str]', work: 'Union[Config.Object, str]'):
        """
        Assigns work to the client group

        Args:
            group: The :ref:`config_object` or name of the client group.
            work: The :ref:`config_object` or name of the work.
        """
        group_dn = self._get_dn(group, parent_dn=self._group_base_dn)
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        response = self._api.websdk.Config.Write.post(
            object_dn=group_dn,
            attribute_data=self._name_value_list({
                ClientGroupAttributes.assigned_work: [work_dn]
            })
        )

        if response.result.code != 1:
            raise InvalidResultCode(code=response.result.code,
                                                 code_description=response.result.credential_result)

    def delete(self, group: 'Union[Config.Object, str]'):
        """
        Deletes a client group

        Args:
            group: :ref:`config_object` or name of the client group.
        """
        group_dn = self._get_dn(group, parent_dn=self._group_base_dn)
        self._config_delete(object_dn=group_dn)

    def get(self, name: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            name: The name of the client group.
            raise_error_if_not_exists: Raise an exception if the client group does not exist.

        Returns:
            :ref:`config_object` of the client group.
        """
        return self._get_config_object(
            object_dn=fr'{self._group_base_dn}\{name}',
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def list(self):
        """
        Lists all client groups.

        Returns:
            List of :ref:`config_object` of the client groups.
        """
        response = self._api.websdk.Config.Enumerate.post(object_dn=self._group_base_dn)

        if response.result.code != 1:
            raise InvalidResultCode(
                code=response.result.code,
                code_description=response.result.credential_result
            )
        return response.objects

    def remove_work(self, group: 'Union[Config.Object, str]', work: 'Union[Config.Object, str]'):
        """
        Removes work from a client group

        Args:
            group: The :ref:`config_object` or name of the client group.
            work: The :ref:`config_object` or name of the work to be removed.
        """
        group_dn = self._get_dn(group, parent_dn=self._group_base_dn)
        work_dn = self._get_dn(work, parent_dn=self._work_base_dn)
        response = self._api.websdk.Config.RemoveDnValue.post(
            object_dn=group_dn,
            attribute_name=ClientGroupAttributes.assigned_work,
            value=work_dn
        )
        if response.result.code != 1:
            raise InvalidResultCode(
                code=response.result.code,
                code_description=response.result.credential_result
            )


@feature('Agentless Group')
class Agentless(_ClientGroupBase):
    def create(self, name: str, get_if_already_exists: bool = True):
        """
        Args:
            name: The name of the client group.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the client group.
        """
        attributes = {
            ClientGroupAttributes.created_by: ClientGroupsAttributeValues.CreatedBy.websdk,
            ClientGroupAttributes.agent_type: ClientGroupsAttributeValues.AgentType.agentless,
            ClientGroupAttributes.rule      : ClientGroupsAttributeValues.DefaultRules.agentless
        }

        return self._config_create(
            name=name,
            parent_folder_dn=self._group_base_dn,
            config_class=ClientGroupAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature('EST Certificate Enrollment Group')
class EstCertificateEnrollment(_ClientGroupBase):
    def create(self, name: str, get_if_already_exists: bool = True):
        """
        Args:
            name: The name of the client group.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the client group.
        """
        attributes = {
            ClientGroupAttributes.created_by: ClientGroupsAttributeValues.CreatedBy.websdk,
            ClientGroupAttributes.agent_type: ClientGroupsAttributeValues.AgentType.est,
            ClientGroupAttributes.rule      : ClientGroupsAttributeValues.DefaultRules.est
        }

        return self._config_create(
            name=name,
            parent_folder_dn=self._group_base_dn,
            config_class=ClientGroupAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )


@feature('Venafi Agent Group')
class VenafiAgent(_ClientGroupBase):
    def create(self, name: str, get_if_already_exists: bool = True):
        """
        Args:
            name: The name of the client group.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the client group.
        """
        attributes = {
            ClientGroupAttributes.created_by: ClientGroupsAttributeValues.CreatedBy.websdk,
            ClientGroupAttributes.agent_type: ClientGroupsAttributeValues.AgentType.venafi_agent,
            ClientGroupAttributes.rule      : ClientGroupsAttributeValues.DefaultRules.venafi_agent
        }

        return self._config_create(
            name=name,
            parent_folder_dn=self._group_base_dn,
            config_class=ClientGroupAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

