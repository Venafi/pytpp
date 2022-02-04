from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.connection_base import ConnectionBaseAttributes
from pytpp.attributes.ssh_device_base import SshDeviceBaseAttributes
from pytpp.attributes.top import TopAttributes
from pytpp.attributes.validation_base import ValidationBaseAttributes


class DeviceAttributes(ConnectionBaseAttributes, SshDeviceBaseAttributes, TopAttributes, ValidationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Device"
	agentless_discovery_stage = Attribute('Agentless Discovery Stage', min_version='15.2')
	agentless_discovery_status = Attribute('Agentless Discovery Status', min_version='15.2')
	allow_agentless_discovery_and_remediation = Attribute('Allow Agentless Discovery and Remediation', min_version='15.2')
	approver = Attribute('Approver', min_version='17.3')
	bulk_provisioning_dn = Attribute('Bulk Provisioning Dn', min_version='18.3')
	bulk_provisioning_stage = Attribute('Bulk Provisioning Stage', min_version='18.3')
	bulk_provisioning_status = Attribute('Bulk Provisioning Status', min_version='18.3')
	client_id = Attribute('Client ID')
	client_machine_id = Attribute('Client Machine ID', min_version='17.1')
	cloud_instance_id = Attribute('Cloud Instance ID', min_version='17.1')
	cloud_region = Attribute('Cloud Region', min_version='17.1')
	cloud_service = Attribute('Cloud Service', min_version='17.1')
	created_by = Attribute('Created By', min_version='15.1')
	deny_multiple_authentication_failures = Attribute('Deny Multiple Authentication Failures', min_version='19.4')
	disabled_on = Attribute('Disabled On', min_version='17.1')
	discovered_by_dn = Attribute('Discovered By DN', min_version='19.1')
	jump_server_dn = Attribute('Jump Server DN')
	last_attempt_to_get_client_subsystem_record = Attribute('Last Attempt To Get Client Subsystem Record', min_version='17.1')
	last_discovery_date = Attribute('Last Discovery Date', min_version='15.2')
	last_discovery_planned = Attribute('Last Discovery Planned', min_version='16.4')
	last_discovery_platform_version = Attribute('Last Discovery Platform Version', min_version='20.2')
	last_file_operations_platform_version = Attribute('Last File Operations Platform Version', min_version='20.2')
	location = Attribute('Location')
	manual_approval = Attribute('Manual Approval')
	maximum_authorizations_per_keyset = Attribute('Maximum Authorizations Per Keyset', min_version='20.1')
	onboard_discovery_dn = Attribute('Onboard Discovery Dn', min_version='16.1')
	onboard_discovery_stage = Attribute('Onboard Discovery Stage', min_version='16.1')
	onboard_discovery_status = Attribute('Onboard Discovery Status', min_version='16.1')
	onboard_discovery_to_do = Attribute('Onboard Discovery To Do', min_version='16.1')
	placement_job_dn = Attribute('Placement Job Dn', min_version='16.3')
	previous_connection_credential_hash = Attribute('Previous Connection Credential Hash', min_version='19.4')
	privilege_elevation_command = Attribute('Privilege Elevation Command', min_version='17.1')
	protection_key = Attribute('Protection Key')
	required_sync_confirmation = Attribute('Required Sync Confirmation', min_version='19.2')
	ssh_key_encryption = Attribute('SSH Key Encryption', min_version='16.4')
	status = Attribute('Status')
	system_owned_keys = Attribute('System Owned Keys', min_version='15.4')
