from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.discovery_statistics import DiscoveryStatisticsAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.top import TopAttributes


class AgentDiscoveryBaseAttributes(DiscoveryStatisticsAttributes, ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent Discovery Base"
	configuration = Attribute('Configuration')
	discovery_exclusion_dn = Attribute('Discovery Exclusion DN')
	protection_key = Attribute('Protection Key')
	report_dn = Attribute('Report DN')
	status = Attribute('Status')
