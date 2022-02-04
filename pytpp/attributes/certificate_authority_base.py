from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class CertificateAuthorityBaseAttributes(DriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Certificate Authority Base"
	additional_field = Attribute('Additional Field')
	concurrent_connection_limit = Attribute('Concurrent Connection Limit')
	credential = Attribute('Credential')
	credits = Attribute('Credits')
	credits_alert = Attribute('Credits Alert')
	credits_used = Attribute('Credits Used')
	enhanced_key_usage = Attribute('Enhanced Key Usage', min_version='19.2')
	host = Attribute('Host')
	manual_approval = Attribute('Manual Approval')
	port = Attribute('Port')
	protection_key = Attribute('Protection Key')
	renewal_window = Attribute('Renewal Window')
	retry_count = Attribute('Retry Count')
	retry_interval = Attribute('Retry Interval')
	san_enabled = Attribute('SAN Enabled')
	signature_algorithm = Attribute('Signature Algorithm')
	specific_end_date_enabled = Attribute('Specific End Date Enabled')
	template = Attribute('Template')
	test_account = Attribute('Test Account')
	timeout = Attribute('Timeout')
	validity_period = Attribute('Validity Period')
	vault_id = Attribute('Vault Id')
