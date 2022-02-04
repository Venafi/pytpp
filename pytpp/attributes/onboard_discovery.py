from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.top import TopAttributes


class OnboardDiscoveryAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Onboard Discovery"
	amazon_account_ids = Attribute('Amazon Account Ids', min_version='19.2')
	application_type = Attribute('Application Type', min_version='15.2')
	azure_application_id = Attribute('Azure Application Id', min_version='19.2')
	azure_tenant_id = Attribute('Azure Tenant Id', min_version='19.2')
	certificates_placement_folder = Attribute('Certificates Placement Folder', min_version='15.2')
	credential = Attribute('Credential', min_version='18.4')
	default_container = Attribute('Default Container', min_version='15.2')
	device = Attribute('Device', min_version='15.2')
	devices_folder = Attribute('Devices Folder', min_version='15.2')
	disable_installations_not_in_use = Attribute('Disable Installations Not In Use', min_version='21.4')
	driver_name = Attribute('Driver Name', min_version='15.2')
	environment = Attribute('Environment', min_version='20.2')
	extract_private_key = Attribute('Extract Private Key', min_version='15.2')
	in_progress = Attribute('In Progress', min_version='15.2')
	last_run = Attribute('Last Run', min_version='18.2')
	last_update = Attribute('Last Update', min_version='15.2')
	log_debug = Attribute('Log Debug', min_version='19.3')
	onboard_discovery_import_work_to_do = Attribute('Onboard Discovery Import Work To Do', min_version='15.2')
	port = Attribute('Port', min_version='18.1')
	profiles_to_import = Attribute('Profiles To Import', min_version='16.1')
	result_count = Attribute('Result Count', min_version='15.2')
	script_execution_timeout = Attribute('Script Execution Timeout', min_version='20.2')
	script_hash_mismatch_error = Attribute('Script Hash Mismatch Error', min_version='18.4')
	status = Attribute('Status', min_version='15.2')
	stop_requested = Attribute('Stop Requested', min_version='15.2')
	timeout = Attribute('Timeout', min_version='19.2')
	xml_port = Attribute('XML Port', min_version='18.2')
