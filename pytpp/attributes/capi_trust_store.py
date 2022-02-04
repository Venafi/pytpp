from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class CAPITrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "CAPI Trust Store"
	log_windows_events = Attribute('Log Windows Events')
	trust_store_name = Attribute('Trust Store Name', min_version='20.1')
