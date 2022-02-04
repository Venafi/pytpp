from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class GlobalSignMSSLCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "GlobalSign MSSL CA"
	domain_id = Attribute('Domain ID')
	profile_id = Attribute('Profile ID')
	san_type = Attribute('SAN Type')
	web_service_url = Attribute('Web Service URL')
