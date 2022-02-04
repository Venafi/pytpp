from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.service_module import ServiceModuleAttributes


class MonitoringModuleAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Monitoring Module"
	escalation_notice_interval = Attribute('Escalation Notice Interval')
	escalation_notice_start = Attribute('Escalation Notice Start')
	expiration_notice_interval = Attribute('Expiration Notice Interval')
	expiration_notice_start = Attribute('Expiration Notice Start')
