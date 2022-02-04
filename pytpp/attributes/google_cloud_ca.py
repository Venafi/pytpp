from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class GoogleCloudCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Google Cloud CA"
	certificate_authority_id = Attribute('Certificate Authority ID', min_version='20.2')
	region = Attribute('Region', min_version='20.4')
