from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.service_module import ServiceModuleAttributes


class CertificateManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Certificate Manager"
	cdp_aia_verification_disabled = Attribute('CDP AIA Verification Disabled')
	certificate_api_todo_timeout = Attribute('Certificate API ToDo Timeout', min_version='21.4')
	escalation_notice_interval = Attribute('Escalation Notice Interval')
	escalation_notice_start = Attribute('Escalation Notice Start')
	expiration_notice_interval = Attribute('Expiration Notice Interval')
	expiration_notice_start = Attribute('Expiration Notice Start')
	maximum_threads = Attribute('Maximum Threads')
	minimum_threads = Attribute('Minimum Threads')
	renewal_window = Attribute('Renewal Window')
	renewal_window_event = Attribute('Renewal Window Event')
	revocation_check_disabled = Attribute('Revocation Check Disabled')
	service_module_classes = Attribute('Service Module Classes')
	start_time = Attribute('Start Time')
	trust_store_management_disabled = Attribute('Trust Store Management Disabled')
