from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes
from pytpp.attributes.proxy import ProxyAttributes


class AdaptableCAAttributes(CertificateAuthorityBaseAttributes, ProxyAttributes, metaclass=IterableMeta):
	__config_class__ = "Adaptable CA"
	allow_reissue = Attribute('Allow Reissue', min_version='16.2')
	certificate_credential = Attribute('Certificate Credential', min_version='16.2')
	connection_valid = Attribute('Connection Valid', min_version='16.2')
	custom_fields = Attribute('Custom Fields', min_version='16.2')
	interoperability_script = Attribute('Interoperability Script', min_version='16.2')
	log_debug = Attribute('Log Debug', min_version='19.3')
	powershell_script_hash_vault_id = Attribute('PowerShell Script Hash Vault Id', min_version='18.4')
	profile_string = Attribute('Profile String', min_version='20.1')
	renewal_window = Attribute('Renewal Window', min_version='16.2')
	retry_after_script_hash_mismatch = Attribute('Retry After Script Hash Mismatch', min_version='18.4')
	script_execution_timeout = Attribute('Script Execution Timeout', min_version='20.2')
	secondary_credential = Attribute('Secondary Credential', min_version='17.4')
	service_address = Attribute('Service Address', min_version='20.1')
