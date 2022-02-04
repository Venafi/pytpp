from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes


class CodeSigningAppleEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Apple Environment"
	cn_pattern = Attribute('CN Pattern', min_version='21.2')
	certificate_dn = Attribute('Certificate DN', min_version='21.2')
	key_storage_location = Attribute('Key Storage Location', min_version='21.2')
