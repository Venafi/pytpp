from pytpp.attributes._helper import IterableMeta, Attribute


class AgentSSHBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Agent SSH Base"
	credential = Attribute('Credential')
	exclude_remote_mount_points = Attribute('Exclude Remote Mount Points')
	expiration = Attribute('Expiration')
	file_scan_disabled = Attribute('File Scan Disabled')
	log_threshold = Attribute('Log Threshold')
	max_filesize = Attribute('Max Filesize')
	min_filesize = Attribute('Min Filesize')
	port_validation_disabled = Attribute('Port Validation Disabled')
	ssh_scanner_service_path = Attribute('SSH Scanner Service Path')
	ssh_scanner_user_path = Attribute('SSH Scanner User Path')
	sshd_filename_filter = Attribute('SSHd Filename Filter')
	sshd_max_filesize = Attribute('SSHd Max Filesize')
	server_path_defaults_disabled = Attribute('Server Path Defaults Disabled')
	upload_private_keys_disabled = Attribute('Upload Private Keys Disabled')
	user_path_defaults_disabled = Attribute('User Path Defaults Disabled')
