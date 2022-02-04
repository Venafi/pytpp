from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class AdaptableFlowActionBaseAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Adaptable Flow Action Base"
	adaptable_script_max_file_size = Attribute('Adaptable Script Max File Size', min_version='21.4')
	adaptable_script_try_later_max_attempts = Attribute('Adaptable Script Try Later Max Attempts', min_version='21.4')
	adaptable_scripts_directory_name = Attribute('Adaptable Scripts Directory Name', min_version='21.4')
	log_debug = Attribute('Log Debug', min_version='21.4')
	oauth_token_application_id = Attribute('OAuth Token Application Id', min_version='21.4')
	oauth_token_credential = Attribute('OAuth Token Credential', min_version='21.4')
	oauth_token_scope = Attribute('OAuth Token Scope', min_version='21.4')
	powershell_script = Attribute('PowerShell Script', min_version='21.4')
	powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id', min_version='21.4')
	script_execution_timeout = Attribute('Script Execution Timeout', min_version='21.4')
