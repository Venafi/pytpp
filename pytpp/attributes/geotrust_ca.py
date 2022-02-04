from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class GeotrustCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Geotrust CA"
	account_type = Attribute('Account Type')
	address = Attribute('Address')
	billing_contact_first_name = Attribute('Billing Contact First Name')
	billing_contact_internet_email_address = Attribute('Billing Contact Internet EMail Address')
	billing_contact_last_name = Attribute('Billing Contact Last Name')
	billing_contact_telephone_number = Attribute('Billing Contact Telephone Number')
	city = Attribute('City')
	country = Attribute('Country')
	interval = Attribute('Interval')
	organization = Attribute('Organization')
	partner_code = Attribute('Partner Code')
	postal_code = Attribute('Postal Code')
	state = Attribute('State')
	technical_contact_address = Attribute('Technical Contact Address')
	technical_contact_city = Attribute('Technical Contact City')
	technical_contact_country = Attribute('Technical Contact Country')
	technical_contact_first_name = Attribute('Technical Contact First Name')
	technical_contact_internet_email_address = Attribute('Technical Contact Internet EMail Address')
	technical_contact_last_name = Attribute('Technical Contact Last Name')
	technical_contact_organization = Attribute('Technical Contact Organization')
	technical_contact_postal_code = Attribute('Technical Contact Postal Code')
	technical_contact_state = Attribute('Technical Contact State')
	technical_contact_telephone_number = Attribute('Technical Contact Telephone Number')
	technical_contact_title = Attribute('Technical Contact Title')
	telephone_number = Attribute('Telephone Number')
	test_account = Attribute('Test Account')
	web_service_url = Attribute('Web Service URL')
