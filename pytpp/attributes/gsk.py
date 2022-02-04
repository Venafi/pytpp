from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class GSKAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "GSK"
	backup_store = Attribute('Backup Store')
	certificate_label = Attribute('Certificate Label')
	create_store = Attribute('Create Store')
	default_cert = Attribute('Default Cert')
	disable_ssh_history = Attribute('Disable SSH History', min_version='19.1')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
	fips_key = Attribute('Fips Key')
	hide_command_line_passwords = Attribute('Hide Command Line Passwords', min_version='19.4')
	java_home_path = Attribute('Java Home Path')
	key_store = Attribute('Key Store')
	key_store_credential = Attribute('Key Store Credential')
	key_store_validation_disabled = Attribute('Key Store Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	password_expire_days = Attribute('Password Expire Days')
	recycle_alias = Attribute('Recycle Alias')
	refresh_security = Attribute('Refresh Security')
	replace_store = Attribute('Replace Store')
	stash_password = Attribute('Stash Password')
	store_type = Attribute('Store Type')
	temp_certificate_label = Attribute('Temp Certificate Label')
	utility_path = Attribute('Utility Path')
	version = Attribute('Version')
