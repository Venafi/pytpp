from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogChannelContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Channel Container"
	description = Attribute('Description')
