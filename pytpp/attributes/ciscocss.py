from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class CiscoCSSAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "CiscoCSS"
	certificate_file = Attribute('Certificate File')
	chain_cert = Attribute('Chain Cert')
	ftp_credential = Attribute('FTP Credential')
	ftp_host = Attribute('FTP Host')
	ftp_path = Attribute('FTP Path')
	ftp_port = Attribute('FTP Port')
	ftp_record = Attribute('FTP Record')
	ftp_type = Attribute('FTP Type')
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	private_key_file = Attribute('Private Key File')
	reuse_private_key = Attribute('Reuse Private Key')
	ssl_proxy_list = Attribute('SSL Proxy List')
	ssl_server = Attribute('SSL Server')
	server_type = Attribute('Server Type')
	temp_certificate_label = Attribute('Temp Certificate Label')
