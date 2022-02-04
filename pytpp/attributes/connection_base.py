from pytpp.attributes._helper import IterableMeta, Attribute


class ConnectionBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Connection Base"
	concurrent_connection_limit = Attribute('Concurrent Connection Limit')
	connection_method = Attribute('Connection Method')
	credential = Attribute('Credential')
	enforce_known_host = Attribute('Enforce Known Host', min_version='15.2')
	global_sudo = Attribute('Global sudo', min_version='15.3')
	host = Attribute('Host')
	last_known_fingerprint = Attribute('Last Known Fingerprint', min_version='15.2')
	last_known_key_type = Attribute('Last Known Key Type', min_version='17.1')
	port = Attribute('Port')
	remote_server_type = Attribute('Remote Server Type')
	secondary_credential = Attribute('Secondary Credential', min_version='15.3')
	sudo_password_delay = Attribute('Sudo Password Delay', min_version='17.1')
	temp_directory = Attribute('Temp Directory')
	terminal_columns = Attribute('Terminal Columns')
	terminal_rows = Attribute('Terminal Rows')
	terminal_type = Attribute('Terminal Type')
	timeout = Attribute('Timeout')
	trusted_fingerprint = Attribute('Trusted Fingerprint', min_version='15.2')
	trusted_key_type = Attribute('Trusted Key Type', min_version='17.1')
