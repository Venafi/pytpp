from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class F5LTMAdvancedTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    certificate_name = Attribute('Certificate Name')
    ssh_port = Attribute('SSH Port')
    use_rest_api = Attribute('Use REST API', min_version='22.1')
