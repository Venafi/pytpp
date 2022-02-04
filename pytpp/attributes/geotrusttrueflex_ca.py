from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class GeotrustTrueFlexCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "GeotrustTrueFlex CA"
	certificate_block = Attribute('Certificate Block', min_version='15.3')
	certificate_transparency = Attribute('Certificate Transparency', min_version='16.3')
	server_type = Attribute('Server Type', min_version='15.3')
