from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class F5LTMAdvancedTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "F5 LTM Advanced Trust Store"
	certificate_name = Attribute('Certificate Name')
	ssh_port = Attribute('SSH Port')
