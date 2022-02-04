from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class NetScalerAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "NetScaler"
	certificate_file = Attribute('Certificate File')
	chain_cert = Attribute('Chain Cert')
	file_validation_disabled = Attribute('File Validation Disabled')
	fips_key = Attribute('Fips Key')
	import_only = Attribute('Import Only')
	install_path = Attribute('Install Path', min_version='20.2')
	issuer_certificate_name = Attribute('Issuer Certificate Name', min_version='15.1')
	max_filesize = Attribute('Max Filesize')
	network_validation_disabled = Attribute('Network Validation Disabled')
	private_key_file = Attribute('Private Key File')
	sni_certificate = Attribute('SNI Certificate', min_version='17.1')
	ssl_object_type = Attribute('SSL Object Type', min_version='17.1')
	temp_certificate_label = Attribute('Temp Certificate Label')
	virtual_server_name = Attribute('Virtual Server Name')
