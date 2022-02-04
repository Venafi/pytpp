from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class PEMTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "PEM Trust Store"
	key_store = Attribute('Key Store')
