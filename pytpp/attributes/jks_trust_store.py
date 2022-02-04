from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class JKSTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "JKS Trust Store"
	key_store = Attribute('Key Store')
	key_store_credential = Attribute('Key Store Credential')
	store_type = Attribute('Store Type')
