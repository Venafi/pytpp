from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogFilterAttributes(LogChannelAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Filter"
	filter_ids = Attribute('Filter IDs')
	filter_severity = Attribute('Filter Severity')
	log_channel = Attribute('Log Channel')
