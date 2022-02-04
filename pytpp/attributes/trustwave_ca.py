from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class TrustwaveCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Trustwave CA"
	interval = Attribute('Interval')
	reseller_id = Attribute('Reseller ID')
	retrieval_period = Attribute('Retrieval Period')
	web_service_url = Attribute('Web Service URL')
