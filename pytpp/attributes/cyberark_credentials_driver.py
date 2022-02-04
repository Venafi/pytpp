from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_driver_base import CredentialDriverBaseAttributes


class CyberArkCredentialsDriverAttributes(CredentialDriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "CyberArk Credentials Driver"
	central_credential_provider_web_service_url = Attribute('Central Credential Provider Web Service URL', min_version='21.4')
	password_retrieval_method = Attribute('Password Retrieval Method', min_version='21.4')
	scim_server_url = Attribute('SCIM Server URL', min_version='19.3')
	scim_server_user = Attribute('SCIM Server User', min_version='19.3')
	use_proxy = Attribute('Use Proxy', min_version='18.1')
	web_service_url = Attribute('Web Service URL', min_version='17.2')
	web_service_user = Attribute('Web Service User', min_version='17.2')
	windows_credential_provider_version = Attribute('Windows Credential Provider Version', min_version='21.4')
