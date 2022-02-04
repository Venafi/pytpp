from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class ComodoCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Comodo CA"
	address = Attribute('Address')
	company_number = Attribute('Company Number')
	domain_control_validation = Attribute('Domain Control Validation')
	domain_control_validation_email = Attribute('Domain Control Validation Email')
	postal_code = Attribute('Postal Code')
	uri = Attribute('URI')
