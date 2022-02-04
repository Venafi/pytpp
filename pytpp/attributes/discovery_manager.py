from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.discovery_statistics import DiscoveryStatisticsAttributes
from pytpp.attributes.service_module import ServiceModuleAttributes


class DiscoveryManagerAttributes(DiscoveryStatisticsAttributes, ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Discovery Manager"
	connection_timeout = Attribute('Connection Timeout')
	delay = Attribute('Delay')
	load_percentage = Attribute('Load Percentage')
	max_work_units = Attribute('Max Work Units')
	maximum_threads = Attribute('Maximum Threads')
	minimum_threads = Attribute('Minimum Threads')
	placement_disabled = Attribute('Placement Disabled', min_version='16.2')
	timeout = Attribute('Timeout')
	window_days_of_week = Attribute('Window Days of Week')
	window_end = Attribute('Window End')
	window_start = Attribute('Window Start')
