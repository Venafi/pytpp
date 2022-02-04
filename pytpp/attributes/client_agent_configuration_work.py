from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class ClientAgentConfigurationWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Agent Configuration Work"
	agent_cert_trust_bundle = Attribute('Agent Cert Trust Bundle')
	days_of_month = Attribute('Days Of Month')
	days_of_week = Attribute('Days Of Week')
	event_row_count = Attribute('Event Row Count', min_version='15.4')
	interval = Attribute('Interval')
	log_communications = Attribute('Log Communications', min_version='15.4')
	log_facility = Attribute('Log Facility')
	log_threshold = Attribute('Log Threshold')
	minimum_free_space = Attribute('Minimum Free Space')
	proxy_credential = Attribute('Proxy Credential')
	proxy_host = Attribute('Proxy Host')
	schedule_type = Attribute('Schedule Type')
	start_time = Attribute('Start Time')
	tls_crl_verify = Attribute('TLS CRL Verify', min_version='15.4')
	web_service_url = Attribute('Web Service URL')
