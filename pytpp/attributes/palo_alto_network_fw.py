from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class PaloAltoNetworkFWAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Palo Alto Network FW"
	certificate_only = Attribute('Certificate Only', min_version='15.1')
	chain_cert = Attribute('Chain Cert', min_version='15.1')
	create_decryption_policy = Attribute('Create Decryption Policy', min_version='15.1')
	decryption_destinations = Attribute('Decryption Destinations', min_version='15.1')
	decryption_policy = Attribute('Decryption Policy', min_version='15.1')
	decryption_profile = Attribute('Decryption Profile', min_version='15.1')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.1')
	lock_config = Attribute('Lock Config', min_version='15.1')
	network_validation_disabled = Attribute('Network Validation Disabled', min_version='15.1')
	replace_store = Attribute('Replace Store', min_version='15.1')
	tls_service_profile = Attribute('TLS Service Profile', min_version='20.4')
	temporary_name = Attribute('Temporary Name', min_version='15.1')
