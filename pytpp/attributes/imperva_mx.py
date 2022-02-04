from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class ImpervaMXAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Imperva MX"
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
	key_store_validation_disabled = Attribute('Key Store Validation Disabled')
	private_key_name = Attribute('Private Key Name')
	server_group = Attribute('Server Group')
	service = Attribute('Service')
	site = Attribute('Site')
	username_credential = Attribute('Username Credential')
	utility_path = Attribute('Utility Path')
