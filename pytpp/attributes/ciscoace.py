from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class CiscoACEAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "CiscoACE"
	certificate_file = Attribute('Certificate File')
	class_map = Attribute('Class Map')
	context_name = Attribute('Context Name')
	file_validation_disabled = Attribute('File Validation Disabled')
	import_only = Attribute('Import Only')
	include_root_chain = Attribute('Include Root Chain')
	network_validation_disabled = Attribute('Network Validation Disabled')
	non_exportable = Attribute('Non-Exportable')
	policy_map = Attribute('Policy Map')
	private_key_file = Attribute('Private Key File')
	sftp_credential = Attribute('SFTP Credential')
	sftp_host = Attribute('SFTP Host')
	sftp_path = Attribute('SFTP Path')
	sftp_port = Attribute('SFTP Port')
	ssl_proxy_service = Attribute('SSL Proxy Service')
	temp_certificate_label = Attribute('Temp Certificate Label')
