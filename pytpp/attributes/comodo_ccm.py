from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class ComodoCCMAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Comodo CCM"
	customer_login_uri = Attribute('Customer Login URI')
	organization = Attribute('Organization')
	secret_key = Attribute('Secret Key')
