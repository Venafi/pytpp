from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogAdaptableAttributes(LogChannelAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Adaptable"
	adaptable_logging_channel_text_field_1 = Attribute('Adaptable Logging Channel Text Field 1', min_version='17.1')
	adaptable_logging_channel_text_field_10 = Attribute('Adaptable Logging Channel Text Field 10', min_version='17.1')
	adaptable_logging_channel_text_field_11 = Attribute('Adaptable Logging Channel Text Field 11', min_version='17.1')
	adaptable_logging_channel_text_field_12 = Attribute('Adaptable Logging Channel Text Field 12', min_version='17.1')
	adaptable_logging_channel_text_field_2 = Attribute('Adaptable Logging Channel Text Field 2', min_version='17.1')
	adaptable_logging_channel_text_field_3 = Attribute('Adaptable Logging Channel Text Field 3', min_version='17.1')
	adaptable_logging_channel_text_field_4 = Attribute('Adaptable Logging Channel Text Field 4', min_version='17.1')
	adaptable_logging_channel_text_field_5 = Attribute('Adaptable Logging Channel Text Field 5', min_version='17.1')
	adaptable_logging_channel_text_field_6 = Attribute('Adaptable Logging Channel Text Field 6', min_version='17.1')
	adaptable_logging_channel_text_field_7 = Attribute('Adaptable Logging Channel Text Field 7', min_version='17.1')
	adaptable_logging_channel_text_field_8 = Attribute('Adaptable Logging Channel Text Field 8', min_version='17.1')
	adaptable_logging_channel_text_field_9 = Attribute('Adaptable Logging Channel Text Field 9', min_version='17.1')
	credential = Attribute('Credential', min_version='17.1')
	log_debug = Attribute('Log Debug', min_version='19.3')
	oauth_token_application_id = Attribute('OAuth Token Application Id', min_version='21.3')
	oauth_token_credential = Attribute('OAuth Token Credential', min_version='21.3')
	oauth_token_scope = Attribute('OAuth Token Scope', min_version='21.3')
	powershell_script = Attribute('PowerShell Script', min_version='17.1')
	powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id', min_version='18.4')
	script_execution_timeout = Attribute('Script Execution Timeout', min_version='20.2')
	secondary_credential = Attribute('Secondary Credential', min_version='17.4')
	service_address = Attribute('Service Address', min_version='17.1')
