from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.organization import OrganizationAttributes


class PolicyAttributes(OrganizationAttributes, metaclass=IterableMeta):
	__config_class__ = "Policy"
	certificate_origin = Attribute('Certificate Origin', min_version='19.1')
	log_view_server = Attribute('Log View Server')
	master_preferences = Attribute('Master Preferences', min_version='17.2')
	scep_ca_ident = Attribute('Scep CA Ident')
	scep_certificate_authority = Attribute('Scep Certificate Authority')
	scep_challenge_password = Attribute('Scep Challenge Password')
	scep_encryption_ra_certificate = Attribute('Scep Encryption RA Certificate', min_version='18.3')
	scep_intune_application_id = Attribute('Scep Intune Application Id', min_version='19.3')
	scep_intune_application_secret = Attribute('Scep Intune Application Secret', min_version='19.3')
	scep_intune_tenant_name = Attribute('Scep Intune Tenant Name', min_version='19.3')
	scep_ra_certificate = Attribute('Scep RA Certificate')
	scep_selection_rule = Attribute('Scep Selection Rule')
	scep_signing_ra_certificate = Attribute('Scep Signing RA Certificate', min_version='18.3')
