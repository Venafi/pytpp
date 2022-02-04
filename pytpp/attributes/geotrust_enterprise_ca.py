from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class GeotrustEnterpriseCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Geotrust Enterprise CA"
	account_type = Attribute('Account Type')
	address = Attribute('Address')
	city = Attribute('City')
	country = Attribute('Country')
	interval = Attribute('Interval')
	organization = Attribute('Organization')
	partner_code = Attribute('Partner Code')
	postal_code = Attribute('Postal Code')
	state = Attribute('State')
	technical_contact_first_name = Attribute('Technical Contact First Name')
	technical_contact_internet_email_address = Attribute('Technical Contact Internet EMail Address')
	technical_contact_last_name = Attribute('Technical Contact Last Name')
	technical_contact_telephone_number = Attribute('Technical Contact Telephone Number')
	technical_contact_title = Attribute('Technical Contact Title')
	telephone_number = Attribute('Telephone Number')
	test_account = Attribute('Test Account')
	web_service_url = Attribute('Web Service URL')
