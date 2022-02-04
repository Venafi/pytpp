from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class ApacheAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Apache"
	application_id = Attribute('Application ID', min_version='17.2')
	certificate_chain_file = Attribute('Certificate Chain File')
	certificate_file = Attribute('Certificate File')
	client_tools_path = Attribute('Client Tools Path', min_version='17.2')
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	ocs_identifier = Attribute('OCS Identifier', min_version='18.3')
	overwrite_existing_chain = Attribute('Overwrite Existing Chain')
	pbes2_algorithm = Attribute('PBES2 Algorithm', min_version='21.3')
	partition_password_credential = Attribute('Partition Password Credential', min_version='17.2')
	private_key_file = Attribute('Private Key File')
	private_key_label = Attribute('Private Key Label', min_version='19.1')
	private_key_location = Attribute('Private Key Location', min_version='17.2')
	protection_type = Attribute('Protection Type', min_version='18.1')
	slot_number = Attribute('Slot Number', min_version='17.2')
	softcard_identifier = Attribute('Softcard Identifier', min_version='18.1')
