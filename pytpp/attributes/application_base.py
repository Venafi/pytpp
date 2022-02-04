from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.connection_base import ConnectionBaseAttributes
from pytpp.attributes.driver_base import DriverBaseAttributes
from pytpp.attributes.validation_base import ValidationBaseAttributes


class ApplicationBaseAttributes(ConnectionBaseAttributes, DriverBaseAttributes, ValidationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Application Base"
	adaptable_workflow_approvers = Attribute('Adaptable Workflow Approvers', min_version='18.3')
	adaptable_workflow_reference_id = Attribute('Adaptable Workflow Reference ID', min_version='18.3')
	adaptable_workflow_stage = Attribute('Adaptable Workflow Stage', min_version='18.3')
	agent_validate_now = Attribute('Agent Validate Now', min_version='18.2')
	approver = Attribute('Approver')
	certificate = Attribute('Certificate')
	certificate_file = Attribute('Certificate File', min_version='16.2')
	certificate_installed = Attribute('Certificate Installed')
	created_by = Attribute('Created By', min_version='15.1')
	discovered_by_dn = Attribute('Discovered By DN', min_version='19.1')
	discovered_on = Attribute('Discovered On')
	file_owner_group = Attribute('File Owner: Group', min_version='16.3')
	file_owner_user = Attribute('File Owner: User', min_version='16.3')
	file_permissions_enabled = Attribute('File Permissions Enabled', min_version='16.3')
	file_permissions_group = Attribute('File Permissions: Group', min_version='16.3')
	file_permissions_user = Attribute('File Permissions: User', min_version='16.3')
	grouping_id = Attribute('Grouping Id', min_version='15.3')
	in_error = Attribute('In Error')
	in_process = Attribute('In Process', min_version='15.3')
	key_encryption_algorithm = Attribute('Key Encryption Algorithm')
	key_store_vault_id = Attribute('Key Store Vault Id', min_version='15.3')
	last_pushed_by = Attribute('Last Pushed By', min_version='16.2')
	last_pushed_on = Attribute('Last Pushed On', min_version='16.2')
	private_key_password_credential = Attribute('Private Key Password Credential')
	remote_one_to_many_generation = Attribute('Remote One To Many Generation', min_version='19.4')
	restart_application = Attribute('Restart Application')
	stage = Attribute('Stage')
	status = Attribute('Status')
	ticket_dn = Attribute('Ticket DN')
