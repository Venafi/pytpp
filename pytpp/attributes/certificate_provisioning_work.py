from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class CertificateProvisioningWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Certificate Provisioning Work"
	days_of_month = Attribute('Days Of Month', min_version='15.3')
	days_of_week = Attribute('Days Of Week', min_version='15.3')
	interval = Attribute('Interval', min_version='15.3')
	log_threshold = Attribute('Log Threshold', min_version='15.3')
	schedule_type = Attribute('Schedule Type', min_version='15.3')
	start_time = Attribute('Start Time', min_version='15.3')
