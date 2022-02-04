from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.agent_base import AgentBaseAttributes
from pytpp.attributes.top import TopAttributes


class AgentAttributes(AgentBaseAttributes, TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Agent"
	action = Attribute('Action')
	active_directory_dn_host_detail = Attribute('Active Directory DN Host Detail')
	active_directory_domain_host_detail = Attribute('Active Directory Domain Host Detail')
	active_directory_host_details = Attribute('Active Directory Host Details')
	active_directory_query_host_detail = Attribute('Active Directory Query Host Detail')
	active_directory_source_dn_host_detail = Attribute('Active Directory Source DN Host Detail')
	address = Attribute('Address')
	configuration_host_details = Attribute('Configuration Host Details')
	custom_host_detail = Attribute('Custom Host Detail')
	environment_host_details = Attribute('Environment Host Details')
	first_update = Attribute('First Update')
	host_os = Attribute('Host OS')
	hostname = Attribute('Hostname')
	last_update = Attribute('Last Update')
	os_id = Attribute('OS Id')
