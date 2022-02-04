from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class PKCS12Attributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "PKCS#12"
	bundle_certificate = Attribute('Bundle Certificate')
	certificate_chain_file = Attribute('Certificate Chain File')
	certificate_file = Attribute('Certificate File')
	create_store = Attribute('Create Store', min_version='15.1')
	file_validation_disabled = Attribute('File Validation Disabled')
	friendly_name = Attribute('Friendly Name')
	network_validation_disabled = Attribute('Network Validation Disabled')
	recycle_alias = Attribute('Recycle Alias', min_version='15.1')
	replace_store = Attribute('Replace Store', min_version='15.1')
