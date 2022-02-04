from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.code_signing_environment_template_base import CodeSigningEnvironmentTemplateBaseAttributes


class CodeSigningGPGEnvironmentTemplateAttributes(CodeSigningEnvironmentTemplateBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing GPG Environment Template"
	authentication_key_algorithm = Attribute('Authentication Key Algorithm', min_version='20.2')
	encryption_key_algorithm = Attribute('Encryption Key Algorithm', min_version='20.2')
	internet_email_address = Attribute('Internet EMail Address', min_version='20.2')
	key_container_dn = Attribute('Key Container DN', min_version='20.2')
	key_storage_location = Attribute('Key Storage Location', min_version='20.2')
	max_uses = Attribute('Max Uses', min_version='20.2')
	real_name = Attribute('Real Name', min_version='20.2')
	signing_key_algorithm = Attribute('Signing Key Algorithm', min_version='20.2')
	validity_period = Attribute('Validity Period', min_version='20.2')
