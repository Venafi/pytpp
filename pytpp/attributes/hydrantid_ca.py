from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class HydrantIdCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "HydrantId CA"
	api_credentials = Attribute('API Credentials')
	account_name = Attribute('Account Name')
	account_organization = Attribute('Account Organization')
	certificate_type = Attribute('Certificate Type', min_version='15.4')
	subscriber_email = Attribute('Subscriber Email')
	ui_credentials = Attribute('UI Credentials')
	web_service_url = Attribute('Web Service URL')
	web_ui_url = Attribute('Web UI URL')
