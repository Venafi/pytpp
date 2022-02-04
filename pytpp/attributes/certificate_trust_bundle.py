from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CertificateTrustBundleAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Certificate Trust Bundle"
	excluded_certificates = Attribute('Excluded Certificates')
	included_certificates = Attribute('Included Certificates')
	is_match = Attribute('Is Match')
