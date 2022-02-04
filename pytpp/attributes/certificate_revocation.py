from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.service_module import ServiceModuleAttributes


class CertificateRevocationAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Certificate Revocation"
	ca_issuer_monitor_disabled = Attribute('CA Issuer Monitor Disabled', min_version='19.2')
	ocsp_concurrent_connection_limit = Attribute('OCSP Concurrent Connection Limit', min_version='19.2')
	ocsp_concurrent_request_limit = Attribute('OCSP Concurrent Request Limit', min_version='19.2')
