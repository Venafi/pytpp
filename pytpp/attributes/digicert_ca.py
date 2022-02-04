from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class DigiCertCAAttributes(HTTPCABaseAttributes, metaclass=IterableMeta):
	__config_class__ = "DigiCert CA"
	api_credentials = Attribute('API Credentials', min_version='17.3')
	api_key = Attribute('API Key')
	account_number = Attribute('Account Number')
	account_organization = Attribute('Account Organization', min_version='17.3')
	allow_reissue = Attribute('Allow Reissue', min_version='17.3')
	certificate_transparency = Attribute('Certificate Transparency', min_version='18.4')
	division = Attribute('Division', min_version='20.3')
	ev_allowed = Attribute('EV Allowed')
	ev_enabled = Attribute('EV Enabled')
	manual_approval = Attribute('Manual Approval')
	organizational_unit = Attribute('Organizational Unit', min_version='17.3')
	profile_id = Attribute('Profile ID', min_version='15.1')
	renewal_window = Attribute('Renewal Window', min_version='17.3')
	san_enabled = Attribute('SAN Enabled')
	uc_allowed = Attribute('UC Allowed')
	wildcard_allowed = Attribute('Wildcard Allowed')
