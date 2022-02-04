from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.connection_base import ConnectionBaseAttributes
from pytpp.attributes.driver_base import DriverBaseAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes


class BulkApplicationBaseAttributes(ConnectionBaseAttributes, DriverBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Bulk Application Base"
	batch_size = Attribute('Batch Size', min_version='20.1')
	certificate_thumbprint = Attribute('Certificate Thumbprint', min_version='18.3')
	device = Attribute('Device', min_version='18.3')
	exclude_expired_certificates = Attribute('Exclude Expired Certificates', min_version='18.3')
	exclude_historical_certificates = Attribute('Exclude Historical Certificates', min_version='18.3')
	exclude_revoked_certificates = Attribute('Exclude Revoked Certificates', min_version='18.3')
	grouping_id = Attribute('Grouping Id', min_version='18.3')
	in_error = Attribute('In Error', min_version='18.3')
	in_progress = Attribute('In Progress', min_version='18.3')
	last_run = Attribute('Last Run', min_version='18.3')
	last_update = Attribute('Last Update', min_version='18.3')
	light_run = Attribute('Light Run', min_version='18.3')
	light_run_new_certificates_threshold = Attribute('Light Run New Certificates Threshold', min_version='18.3')
	maximum_days_expired = Attribute('Maximum Days Expired', min_version='18.3')
	policydn = Attribute('PolicyDN', min_version='18.3')
	status = Attribute('Status', min_version='18.3')
	stop_requested = Attribute('Stop Requested', min_version='18.3')
