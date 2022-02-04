from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class RemoteAccessRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Remote Access Root"
	approved_issuer = Attribute('Approved Issuer', min_version='19.2')
	authentication_methods = Attribute('Authentication Methods', min_version='19.2')
	certificate_auth_lookup_field = Attribute('Certificate Auth Lookup Field', min_version='19.2')
	certificate_auth_source_field = Attribute('Certificate Auth Source Field', min_version='19.2')
	certificate_auth_source_regex = Attribute('Certificate Auth Source Regex', min_version='19.2')
	certificate_pinning_options = Attribute('Certificate Pinning Options', min_version='19.2')
	certificate_pinning_work_dn = Attribute('Certificate Pinning Work DN', min_version='19.2')
	expiration = Attribute('Expiration', min_version='20.1')
	grant_validity = Attribute('Grant Validity', min_version='19.2')
	mapping_table = Attribute('Mapping Table', min_version='20.1')
	refresh_api_enabled = Attribute('Refresh API Enabled', min_version='20.1')
	refresh_token_enabled = Attribute('Refresh Token Enabled', min_version='19.2')
	session_pool_entries = Attribute('Session Pool Entries', min_version='19.2')
	session_pool_max_age = Attribute('Session Pool Max Age', min_version='19.2')
	session_rights_refresh_age = Attribute('Session Rights Refresh Age', min_version='19.2')
	token_validity = Attribute('Token Validity', min_version='19.2')
