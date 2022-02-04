from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class AdaptableCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Adaptable Credential"
	credential_connector = Attribute('Credential Connector', min_version='21.1')
	credential_type = Attribute('Credential Type', min_version='21.1')
	option_1 = Attribute('Option 1', min_version='21.1')
	option_2 = Attribute('Option 2', min_version='21.1')
	password_1 = Attribute('Password 1', min_version='21.1')
	text_field_1 = Attribute('Text Field 1', min_version='21.1')
	text_field_2 = Attribute('Text Field 2', min_version='21.1')
	text_field_3 = Attribute('Text Field 3', min_version='21.1')
	text_field_4 = Attribute('Text Field 4', min_version='21.1')
	text_field_5 = Attribute('Text Field 5', min_version='21.1')
