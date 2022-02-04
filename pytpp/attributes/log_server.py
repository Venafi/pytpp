from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogServerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Server"
	log_application_container = Attribute('Log Application Container')
	log_channel_container = Attribute('Log Channel Container')
	log_notification_container = Attribute('Log Notification Container')
