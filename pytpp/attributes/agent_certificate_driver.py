from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.agent_certificate_base import AgentCertificateBaseAttributes
from pytpp.attributes.agent_driver_base import AgentDriverBaseAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes


class AgentCertificateDriverAttributes(AgentCertificateBaseAttributes, AgentDriverBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent Certificate Driver"
