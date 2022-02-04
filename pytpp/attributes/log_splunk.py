from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogSplunkAttributes(LogChannelAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Splunk"
	credential = Attribute('Credential')
	host = Attribute('Host')
	index = Attribute('Index')
	port = Attribute('Port')
	source = Attribute('Source')
	timeout = Attribute('Timeout')
	verbose = Attribute('Verbose')
