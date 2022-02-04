from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.bulk_application_base import BulkApplicationBaseAttributes


class AdaptableBulkAppAttributes(BulkApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Adaptable Bulk App"
	log_debug = Attribute('Log Debug', min_version='19.3')
	option_1 = Attribute('Option 1', min_version='18.3')
	option_2 = Attribute('Option 2', min_version='18.3')
	pk_credential = Attribute('PK Credential', min_version='18.3')
	password_1 = Attribute('Password 1', min_version='18.3')
	powershell_script = Attribute('PowerShell Script', min_version='18.3')
	powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id', min_version='18.4')
	script_execution_timeout = Attribute('Script Execution Timeout', min_version='20.2')
	script_hash_mismatch_error = Attribute('Script Hash Mismatch Error', min_version='18.4')
	secondary_credential = Attribute('Secondary Credential', min_version='18.3')
	text_field_1 = Attribute('Text Field 1', min_version='18.3')
	text_field_2 = Attribute('Text Field 2', min_version='18.3')
	text_field_3 = Attribute('Text Field 3', min_version='18.3')
	text_field_4 = Attribute('Text Field 4', min_version='18.3')
	text_field_5 = Attribute('Text Field 5', min_version='18.3')
