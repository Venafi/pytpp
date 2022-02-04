from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.organization import OrganizationAttributes


class AgentModuleHandlerContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent Module Handler Container"
