from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class F5Attributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "F5"
	bundle_certificate = Attribute('Bundle Certificate')
	certificate_chain_name = Attribute('Certificate Chain Name')
	certificate_name = Attribute('Certificate Name')
	file_validation_disabled = Attribute('File Validation Disabled')
	fips_key = Attribute('Fips Key')
	network_validation_disabled = Attribute('Network Validation Disabled')
	overwrite_certificate = Attribute('Overwrite Certificate')
	overwrite_existing_chain = Attribute('Overwrite Existing Chain')
	overwrite_key = Attribute('Overwrite Key')
	private_key_name = Attribute('Private Key Name')
	private_key_type = Attribute('Private Key Type')
	ssh_port = Attribute('SSH Port')
