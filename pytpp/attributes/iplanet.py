from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class iPlanetAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "iPlanet"
	alias = Attribute('Alias')
	certutil_path = Attribute('Certutil Path')
	create_store = Attribute('Create Store')
	create_virtual_server = Attribute('Create Virtual Server')
	database_credential = Attribute('Database Credential')
	database_prefix = Attribute('Database Prefix')
	database_type = Attribute('Database Type', min_version='19.1')
	database_validation_disabled = Attribute('Database Validation Disabled')
	document_root = Attribute('Document Root')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
	install_path = Attribute('Install Path')
	key_store = Attribute('Key Store')
	key_store_credential = Attribute('Key Store Credential')
	mta_host = Attribute('MTA Host')
	network_validation_disabled = Attribute('Network Validation Disabled')
	pk12util_path = Attribute('Pk12util Path')
	protocol = Attribute('Protocol')
	replace_store = Attribute('Replace Store')
	secure_server_name = Attribute('Secure Server Name')
	use_proxy = Attribute('Use Proxy')
	virtual_server_dns_value = Attribute('Virtual Server DNS Value')
	virtual_server_port = Attribute('Virtual Server Port')
	virtual_server_user = Attribute('Virtual Server User')
	web_credential = Attribute('Web Credential')
	web_port = Attribute('Web Port')
