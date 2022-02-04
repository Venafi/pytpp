from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class BrocadeAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Brocade"
	all_cipher_suites = Attribute('All Cipher Suites')
	certificate_file = Attribute('Certificate File')
	chain_cert = Attribute('Chain Cert')
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	private_key_file = Attribute('Private Key File')
	privileged_mode_credential = Attribute('Privileged Mode Credential')
	ssl_profile_name = Attribute('SSL Profile Name')
	selected_cipher_suites = Attribute('Selected Cipher Suites')
	session_cache = Attribute('Session Cache')
	temp_certificate_label = Attribute('Temp Certificate Label')
	virtual_server_name = Attribute('Virtual Server Name')
