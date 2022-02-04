from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class HashiCorpVaultPKIAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "HashiCorp Vault PKI"
	crl_address = Attribute('CRL Address', min_version='20.1')
	create_certificate_authority = Attribute('Create Certificate Authority', min_version='20.1')
	create_pki_role = Attribute('Create PKI Role', min_version='20.1')
	enhanced_key_usage = Attribute('Enhanced Key Usage', min_version='20.1')
	network_validation_disabled = Attribute('Network Validation Disabled', min_version='20.1')
	ocsp_address = Attribute('OCSP Address', min_version='20.1')
	policydn = Attribute('PolicyDN', min_version='20.1')
	role_name = Attribute('Role Name', min_version='20.1')
