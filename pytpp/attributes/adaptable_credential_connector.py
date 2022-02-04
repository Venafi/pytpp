from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_driver_base import CredentialDriverBaseAttributes


class AdaptableCredentialConnectorAttributes(CredentialDriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Adaptable Credential Connector"
	credential = Attribute('Credential', min_version='21.1')
	powershell_script = Attribute('PowerShell Script', min_version='21.1')
	powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id', min_version='21.1')
	web_service_url = Attribute('Web Service URL', min_version='21.1')
