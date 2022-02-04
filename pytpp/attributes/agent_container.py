from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class AgentContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent Container"
