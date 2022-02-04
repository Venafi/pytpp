from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class ClientAgentSSHProvisioningWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Agent SSH Provisioning Work"
	days_of_month = Attribute('Days Of Month', min_version='15.1')
	days_of_week = Attribute('Days Of Week', min_version='15.1')
	interval = Attribute('Interval', min_version='15.1')
	log_threshold = Attribute('Log Threshold', min_version='15.1')
	schedule_type = Attribute('Schedule Type', min_version='15.1')
	start_time = Attribute('Start Time', min_version='15.1')
