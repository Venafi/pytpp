from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class OpenTrustPKICAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "OpenTrust PKI CA"
	connector_type = Attribute('Connector Type')
	fields = Attribute('Fields')
	retrieval_period = Attribute('Retrieval Period')
	web_service_url = Attribute('Web Service URL')
