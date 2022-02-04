from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes


class CodeSigningKeyPairEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Key Pair Environment"
	key_algorithm = Attribute('Key Algorithm', min_version='21.2')
	key_dn = Attribute('Key DN', min_version='21.2')
	key_storage_location = Attribute('Key Storage Location', min_version='21.2')
	max_uses = Attribute('Max Uses', min_version='21.2')
	validity_period = Attribute('Validity Period', min_version='21.2')
