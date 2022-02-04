from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.agent_driver_base import AgentDriverBaseAttributes
from pytpp.attributes.agent_ssh_base import AgentSSHBaseAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes


class AgentSSHDriverAttributes(AgentDriverBaseAttributes, AgentSSHBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent SSH Driver"
