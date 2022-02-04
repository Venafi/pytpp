from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class DataPowerAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "DataPower"
	application_domain = Attribute('Application Domain')
	associate_to_cp = Attribute('Associate To CP')
	certificate_name = Attribute('Certificate Name', min_version='16.1')
	certificate_only = Attribute('Certificate Only')
	chain_cert = Attribute('Chain Cert')
	create_cp = Attribute('Create CP')
	create_ic = Attribute('Create IC')
	create_vc = Attribute('Create VC')
	credential_type = Attribute('Credential Type', min_version='17.3')
	crypto_profile = Attribute('Crypto Profile', min_version='17.3')
	ftp_credential = Attribute('FTP Credential')
	ftp_host = Attribute('FTP Host')
	ftp_path = Attribute('FTP Path')
	ftp_port = Attribute('FTP Port')
	file_validation_disabled = Attribute('File Validation Disabled')
	fips_key = Attribute('Fips Key')
	folder = Attribute('Folder', min_version='17.3')
	max_filesize = Attribute('Max Filesize')
	network_validation_disabled = Attribute('Network Validation Disabled')
	private_key_name = Attribute('Private Key Name', min_version='16.1')
	ssh_prompt = Attribute('SSH Prompt')
	ssl_profile_type = Attribute('SSL Profile Type', min_version='17.3')
	ssl_proxy_profile = Attribute('SSL Proxy Profile')
	temp_certificate_label = Attribute('Temp Certificate Label')
	use_basic_provisioning = Attribute('Use Basic Provisioning', min_version='16.1')
	xml_port = Attribute('XML Port', min_version='17.3')
