from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.service_module import ServiceModuleAttributes


class CloudInstanceMonitorAttributes(ScheduleBaseAttributes, ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Cloud Instance Monitor"
