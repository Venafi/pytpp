from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class TealeafSunimpAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "TealeafSunimp"
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
	key_store_credential = Attribute('Key Store Credential')
	key_store_name = Attribute('Key Store Name')
	key_store_validation_disabled = Attribute('Key Store Validation Disabled')
	sunimp_utility_path = Attribute('Sunimp Utility Path')
	tealeaf_utility_path = Attribute('Tealeaf Utility Path')
