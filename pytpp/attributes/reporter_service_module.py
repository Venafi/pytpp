from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.service_module import ServiceModuleAttributes


class ReporterServiceModuleAttributes(ScheduleBaseAttributes, ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Reporter Service Module"
	host = Attribute('Host')
	log_delivery = Attribute('Log Delivery')
	max_running_reports = Attribute('Max Running Reports', min_version='17.1')
	render_options = Attribute('Render Options', min_version='21.4')
	report_execution_timeout = Attribute('Report Execution Timeout', min_version='17.1')
	report_max_source_record_count = Attribute('Report Max Source Record Count', min_version='17.1')
	smtp_credentials = Attribute('SMTP Credentials')
	secure = Attribute('Secure')
	sender = Attribute('Sender')
