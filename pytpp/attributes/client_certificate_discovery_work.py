from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class ClientCertificateDiscoveryWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Certificate Discovery Work"
	certificate_location_dn = Attribute('Certificate Location DN', min_version='15.2')
	certificate_scanner_capi = Attribute('Certificate Scanner CAPI')
	certificate_scanner_map = Attribute('Certificate Scanner Map')
	certificate_scanner_native = Attribute('Certificate Scanner Native')
	certificate_scanner_native_stores = Attribute('Certificate Scanner Native Stores')
	certificate_scanner_path = Attribute('Certificate Scanner Path')
	clear_cache_timestamp = Attribute('Clear Cache Timestamp', min_version='20.1')
	credential = Attribute('Credential')
	days_of_month = Attribute('Days Of Month')
	days_of_week = Attribute('Days Of Week')
	device_location_dn = Attribute('Device Location DN', min_version='15.2')
	discovery_container = Attribute('Discovery Container')
	exclude_remote_mount_points = Attribute('Exclude Remote Mount Points')
	interval = Attribute('Interval')
	log_threshold = Attribute('Log Threshold')
	max_filesize = Attribute('Max Filesize')
	minimize_resource_use = Attribute('Minimize Resource Use')
	naming_pattern = Attribute('Naming Pattern')
	placement_rule = Attribute('Placement Rule', min_version='15.2')
	placement_summary = Attribute('Placement Summary', min_version='15.2')
	schedule_type = Attribute('Schedule Type')
	start_time = Attribute('Start Time')
	treat_unknown_roots_as_self_signed = Attribute('Treat Unknown Roots As Self Signed', min_version='21.1')
