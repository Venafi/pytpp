from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class AgentDriverBaseAttributes(DriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent Driver Base"
	address = Attribute('Address')
	agent_discovery_redirection_rule = Attribute('Agent Discovery Redirection Rule')
	credential = Attribute('Credential')
	expiration = Attribute('Expiration')
	extended_host_details = Attribute('Extended Host Details')
	interval = Attribute('Interval')
	log_threshold = Attribute('Log Threshold')
	managed_by_discovery_dn = Attribute('Managed By Discovery DN')
	module_disabled = Attribute('Module Disabled')
	port = Attribute('Port')
	version = Attribute('Version')
