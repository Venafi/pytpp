from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class MicrosoftCAPoolAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Microsoft CA Pool"
	certificate_authority = Attribute('Certificate Authority', min_version='19.1')
	second_certificate_authority = Attribute('Second Certificate Authority', min_version='19.1')
	third_certificate_authority = Attribute('Third Certificate Authority', min_version='19.1')
