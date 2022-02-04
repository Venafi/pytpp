from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class A10AXTrafficManagerAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "A10 AX Traffic Manager"
	bundle_certificate = Attribute('Bundle Certificate')
	certificate_chain_name = Attribute('Certificate Chain Name')
	certificate_name = Attribute('Certificate Name')
	file_validation_disabled = Attribute('File Validation Disabled')
	install_chain_file = Attribute('Install Chain File')
	network_validation_disabled = Attribute('Network Validation Disabled')
	ssh_port = Attribute('SSH Port')
	ssl_cache_size = Attribute('SSL Cache Size')
	ssl_close_notification = Attribute('SSL Close Notification')
	ssl_false_start = Attribute('SSL False Start')
	ssl_pass_phrase = Attribute('SSL Pass Phrase')
	ssl_profile_name = Attribute('SSL Profile Name')
	ssl_profile_type = Attribute('SSL Profile Type')
	tls_version = Attribute('TLS Version')
	use_ssl_template = Attribute('Use SSL Template')
