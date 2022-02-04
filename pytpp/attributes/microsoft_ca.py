from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class MicrosoftCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Microsoft CA"
	enrollment_agent_certificate = Attribute('Enrollment Agent Certificate')
	given_name = Attribute('Given Name')
	include_cn_as_san = Attribute('Include CN as SAN')
