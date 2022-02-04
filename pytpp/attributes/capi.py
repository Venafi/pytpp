from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class CAPIAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "CAPI"
	binding_ip_address = Attribute('Binding IP Address')
	binding_port = Attribute('Binding Port')
	create_binding = Attribute('Create Binding')
	crypto_service_provider = Attribute('Crypto Service Provider', min_version='17.2')
	file_validation_disabled = Attribute('File Validation Disabled')
	friendly_name = Attribute('Friendly Name')
	hostname = Attribute('Hostname', min_version='15.4')
	network_validation_disabled = Attribute('Network Validation Disabled')
	non_exportable = Attribute('Non-Exportable')
	private_key_label = Attribute('Private Key Label', min_version='17.4')
	private_key_location = Attribute('Private Key Location', min_version='17.2')
	private_key_trustee = Attribute('Private Key Trustee')
	update_iis = Attribute('Update IIS')
	web_site_name = Attribute('Web Site Name')
