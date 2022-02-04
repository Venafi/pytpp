from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class SelfSignedCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Self Signed CA"
	algorithm = Attribute('Algorithm')
	enhanced_key_usage = Attribute('Enhanced Key Usage')
	key_usage = Attribute('Key Usage')
