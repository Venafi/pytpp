from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes


class CodeSigningGPGEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing GPG Environment"
	authentication_key_algorithm = Attribute('Authentication Key Algorithm', min_version='20.3')
	authentication_key_dn = Attribute('Authentication Key DN', min_version='20.2')
	encryption_key_algorithm = Attribute('Encryption Key Algorithm', min_version='20.3')
	encryption_key_dn = Attribute('Encryption Key DN', min_version='20.2')
	internet_email_address = Attribute('Internet EMail Address', min_version='20.3')
	issuer_key_dn = Attribute('Issuer Key DN', min_version='21.4')
	key_storage_location = Attribute('Key Storage Location', min_version='20.3')
	max_uses = Attribute('Max Uses', min_version='20.3')
	real_name = Attribute('Real Name', min_version='20.3')
	signing_key_algorithm = Attribute('Signing Key Algorithm', min_version='20.3')
	signing_key_dn = Attribute('Signing Key DN', min_version='20.2')
	validity_period = Attribute('Validity Period', min_version='20.3')
