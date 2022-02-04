from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class EntrustPKIGatewayAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Entrust PKI Gateway"
	ca_capabilities = Attribute('CA Capabilities', min_version='20.2')
	ca_name = Attribute('CA Name', min_version='20.2')
	exclude_subjectvariables = Attribute('Exclude SubjectVariables', min_version='20.4')
	profile_capabilities = Attribute('Profile Capabilities', min_version='20.2')
	web_service_url = Attribute('Web Service URL', min_version='20.2')
