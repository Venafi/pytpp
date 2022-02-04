from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class AzureKeyVaultAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Azure Key Vault"
	binding_hostnames = Attribute('Binding Hostnames', min_version='19.2')
	binding_ssl_type = Attribute('Binding SSL Type', min_version='19.2')
	certificate_credential = Attribute('Certificate Credential', min_version='17.2')
	certificate_name = Attribute('Certificate Name', min_version='17.2')
	client_id = Attribute('Client ID', min_version='17.2')
	create_binding = Attribute('Create Binding', min_version='19.2')
	create_san_dns_bindings = Attribute('Create SAN DNS Bindings', min_version='19.2')
	environment = Attribute('Environment', min_version='20.2')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='17.2')
	network_validation_disabled = Attribute('Network Validation Disabled', min_version='17.2')
	non_exportable = Attribute('Non-Exportable', min_version='17.2')
	timeout = Attribute('Timeout', min_version='17.2')
	update_web_app = Attribute('Update Web App', min_version='19.2')
	vault_name = Attribute('Vault Name', min_version='17.2')
	web_app_name = Attribute('Web App Name', min_version='19.2')
