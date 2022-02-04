from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import InvalidResultCode
from pytpp.features.definitions.classes import Classes
from pytpp.attributes.device import DeviceAttributes
from pytpp.attributes.jump_server import JumpServerAttributes
from typing import Union, List, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Config, Identity


class _DeviceBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, device: 'Union[Config.Object, str]'):
        """
        Deletes the device object specified.

        Args:
            device: :ref:`config_object` or :ref:`dn` of to the device object.
        """
        dn = self._get_dn(device)
        self._config_delete(object_dn=dn)


@feature('Device')
class Device(_DeviceBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None, address: 'str' = None, agent_provisioning_mode: 'bool' = None,
               concurrent_connection_limit: 'int' = None, device_credential: 'Union[Config.Object, str]' = None,
               temp_directory: 'str' = None, os_type: 'str' = None, jump_server: 'Union[Config.Object, str]' = None,
               use_sudo: 'bool' = None, sudo_credential: 'Union[Config.Object, str]' = None, enforce_host_key: 'bool' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the device object .
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            description: Description of the device object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` of the contacts.
            address: Hostname or IP address of the device.
            agent_provisioning_mode: Set provisioning mode to connect via Agent if ``True``.
            concurrent_connection_limit: Concurrent connection limit to this device.
            device_credential: :ref:`config_object` or :ref:`dn` of the device credential.
            temp_directory: Temp directory.
            os_type: Operating Sytem type.
            jump_server: :ref:`config_object` or :ref:`dn` of the jump server.
            use_sudo: Use sudo.
            sudo_credential: :ref:`config_object` or :ref:`dn` of the sudo user credential.
            enforce_host_key: Enforce host key policy.
            attributes: List of attributes pertaining to the device object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the device object.
        """
        dev_attrs = {
            DeviceAttributes.description: description,
            DeviceAttributes.contact: [self._get_prefixed_universal(c) for c in contacts] if contacts else None,
            DeviceAttributes.host: address,
            DeviceAttributes.connection_method: {True: "Agent"}.get(agent_provisioning_mode),
            DeviceAttributes.concurrent_connection_limit: concurrent_connection_limit,
            DeviceAttributes.credential: self._get_dn(device_credential) if device_credential else None,
            DeviceAttributes.temp_directory: temp_directory,
            DeviceAttributes.remote_server_type: os_type,
            DeviceAttributes.jump_server_dn: self._get_dn(jump_server) if jump_server else None,
            DeviceAttributes.global_sudo: {True: "1", False: "0"}.get(use_sudo),
            DeviceAttributes.secondary_credential: self._get_dn(sudo_credential) if sudo_credential else None,
            DeviceAttributes.enforce_known_host: {True: "1", False: "0"}.get(enforce_host_key)
        }
        if attributes:
            dev_attrs.update(attributes)

        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=Classes.device,
            attributes=dev_attrs,
            get_if_already_exists=get_if_already_exists
        )

    def get(self, device_dn: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            device_dn: :ref:`dn` of the device object.
            raise_error_if_not_exists: Raise an exception if the device DN does not exist.

        Returns:
            :ref:`config_object` of the device object.
        """
        return self._get_config_object(
            object_dn=device_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def scan_for_ssh_keys(self, device: 'Union[Config.Object, str]'):
        """
        Submits Agentless discovery work for the given device.

        Args:
            device: :ref:`config_object` or :ref:`dn` of the device object.
        """
        dn = self._get_dn(device)
        result = self._api.websdk.Config.Write.post(
            object_dn=dn,
            attribute_data=[{"Name": "Agentless Discovery To Do",
                            "Value": "1"}]
        ).result

        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)


@feature('Jump Server')
class JumpServer(_DeviceBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None, address: 'str' = None, port: 'int' = None,
               concurrent_connection_limit: 'int' = None, device_credential: 'Union[Config.Object, str]' = None,
               temp_directory: 'str' = None, os_type: 'str' = None, ssh_version: 'str' = None, ssh_syntax: 'str' = None,
               use_sudo: 'bool' = None, sudo_credential: 'Union[Config.Object, str]' = None,
               enforce_host_key: 'bool' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the device object .
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            description: Description of the device object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` of the contacts.
            address: Hostname or IP address of the device.
            port: Connection port.
            concurrent_connection_limit: Concurrent connection limit to this device.
            device_credential: :ref:`config_object` or :ref:`dn` of the device credential.
            temp_directory: Temp directory.
            os_type: Operating Sytem type.
            ssh_version: SSH version.
            ssh_syntax: SSH syntax.
            use_sudo: Use sudo.
            sudo_credential: :ref:`config_object` or :ref:`dn` of the sudo user credential.
            enforce_host_key: Enforce host key policy.
            attributes: List of attributes pertaining to the device object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the jump server object.
        """
        dev_attrs = {
            JumpServerAttributes.description                : description,
            JumpServerAttributes.contact                    : [self._get_prefixed_universal(c) for c in contacts] if contacts else None,
            JumpServerAttributes.host                       : address,
            JumpServerAttributes.port                       : port,
            JumpServerAttributes.concurrent_connection_limit: concurrent_connection_limit,
            JumpServerAttributes.credential                 : self._get_dn(device_credential) if device_credential else None,
            JumpServerAttributes.temp_directory             : temp_directory,
            JumpServerAttributes.remote_server_type         : os_type,
            JumpServerAttributes.ssh_version                : ssh_version,
            JumpServerAttributes.ssh_connection_string      : ssh_syntax,
            JumpServerAttributes.global_sudo                : {True: "1", False: "0"}.get(use_sudo),
            JumpServerAttributes.secondary_credential       : self._get_dn(sudo_credential) if sudo_credential else None,
            JumpServerAttributes.enforce_known_host         : {True: "1", False: "0"}.get(enforce_host_key)
        }
        if attributes:
            dev_attrs.update(attributes)

        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=Classes.jump_server,
            attributes=dev_attrs,
            get_if_already_exists=get_if_already_exists
        )

    def get(self, device_dn: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            device_dn: :ref:`dn` of the device object.
            raise_error_if_not_exists: Raise an exception if the device DN does not exist.

        Returns:
            :ref:`config_object` of the device object.
        """
        return self._get_config_object(
            object_dn=device_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def scan_for_ssh_keys(self, device: 'Union[Config.Object, str]'):
        """
        Submits Agentless discovery work for the given device.

        Args:
            device: :ref:`config_object` or :ref:`dn` of the device object.
        """
        dn = self._get_dn(device)
        result = self._api.websdk.Config.Write.post(
            object_dn=dn,
            attribute_data=[{
                                "Name" : "Agentless Discovery To Do",
                                "Value": "1"
                            }]
        ).result

        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)
