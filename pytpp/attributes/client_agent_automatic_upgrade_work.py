from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class ClientAgentAutomaticUpgradeWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Agent Automatic Upgrade Work"
	days_of_month = Attribute('Days Of Month')
	days_of_week = Attribute('Days Of Week')
	force_agent_upgrade = Attribute('Force Agent Upgrade')
	interval = Attribute('Interval')
	schedule_type = Attribute('Schedule Type')
	start_time = Attribute('Start Time')
