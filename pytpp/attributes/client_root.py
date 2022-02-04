from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class ClientRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Root"
	client_enrollment_anonymous_allowed = Attribute('Client Enrollment Anonymous Allowed')
	client_enrollment_default_owner = Attribute('Client Enrollment Default Owner')
	client_enrollment_secret_allowed = Attribute('Client Enrollment Secret Allowed')
	client_enrollment_secret_dn = Attribute('Client Enrollment Secret DN')
	client_portal_signing_certificate = Attribute('Client Portal Signing Certificate', min_version='15.2')
	client_trust_certificate_dn = Attribute('Client Trust Certificate DN')
	client_trust_update = Attribute('Client Trust Update')
	dsn = Attribute('DSN')
	driver_name = Attribute('Driver Name')
	environment_variables = Attribute('Environment Variables')
	identity_variables = Attribute('Identity Variables')
	mac_ignore_list = Attribute('MAC Ignore List', min_version='15.2')
	options = Attribute('Options')
	rolling_code_tolerance = Attribute('Rolling Code Tolerance', min_version='15.4')
	rule = Attribute('Rule')
	trust_level = Attribute('Trust Level')
