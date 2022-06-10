from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class PaloAltoNetworkFWTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    lock_config = Attribute('Lock Config', min_version='15.1')
