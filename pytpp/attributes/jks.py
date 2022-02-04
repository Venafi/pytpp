from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class JKSAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "JKS"
	certificate_label = Attribute('Certificate Label')
	create_store = Attribute('Create Store')
	disable_ssh_history = Attribute('Disable SSH History', min_version='19.3')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
	java_vendor = Attribute('Java Vendor', min_version='18.1')
	key_algorithm = Attribute('Key Algorithm')
	key_store = Attribute('Key Store')
	key_store_credential = Attribute('Key Store Credential')
	key_store_validation_disabled = Attribute('Key Store Validation Disabled')
	keytool_path = Attribute('Keytool Path')
	network_validation_disabled = Attribute('Network Validation Disabled')
	private_key_location = Attribute('Private Key Location', min_version='17.2')
	protection_type = Attribute('Protection Type', min_version='18.1')
	recycle_alias = Attribute('Recycle Alias')
	replace_store = Attribute('Replace Store')
	slot_number = Attribute('Slot Number', min_version='17.2')
	softcard_identifier = Attribute('Softcard Identifier', min_version='18.1')
	store_type = Attribute('Store Type')
	temp_certificate_label = Attribute('Temp Certificate Label')
	version = Attribute('Version')
