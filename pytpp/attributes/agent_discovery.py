from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.agent_discovery_base import AgentDiscoveryBaseAttributes


class AgentDiscoveryAttributes(AgentDiscoveryBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent Discovery"
