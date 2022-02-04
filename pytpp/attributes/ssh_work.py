from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class SSHWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Work"
	days_of_month = Attribute('Days Of Month')
	days_of_week = Attribute('Days Of Week')
	exclude_remote_mount_points = Attribute('Exclude Remote Mount Points')
	interval = Attribute('Interval')
	max_filesize = Attribute('Max Filesize')
	new_device_object_landing = Attribute('New Device Object Landing')
	remediation_interval = Attribute('Remediation Interval')
	remediation_schedule_type = Attribute('Remediation Schedule Type')
	remediation_start_time = Attribute('Remediation Start Time')
	ssh_scanner_service_path = Attribute('SSH Scanner Service Path')
	ssh_scanner_user_path = Attribute('SSH Scanner User Path')
	schedule_type = Attribute('Schedule Type')
	server_path_defaults_disabled = Attribute('Server Path Defaults Disabled')
	start_time = Attribute('Start Time')
	user_path_defaults_disabled = Attribute('User Path Defaults Disabled')
