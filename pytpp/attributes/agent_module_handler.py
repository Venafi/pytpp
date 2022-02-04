from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class AgentModuleHandlerAttributes(DriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent Module Handler"
	version = Attribute('Version')
