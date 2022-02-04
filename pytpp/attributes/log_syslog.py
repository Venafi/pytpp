from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogSyslogAttributes(LogChannelAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Syslog"
	credential = Attribute('Credential', min_version='19.3')
	enable_tls = Attribute('Enable TLS', min_version='19.3')
	facility = Attribute('Facility')
	message_format = Attribute('Message Format', min_version='19.3')
	message_prefix = Attribute('Message Prefix', min_version='19.3')
	port = Attribute('Port', min_version='19.3')
	protocol = Attribute('Protocol', min_version='19.3')
	target = Attribute('Target')
	timeout = Attribute('Timeout', min_version='19.3')
