from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.identity_driver import IdentityDriverAttributes


class ActiveDirectoryIdentityDriverAttributes(IdentityDriverAttributes, metaclass=IterableMeta):
	__config_class__ = "ActiveDirectory Identity Driver"
	base_dn = Attribute('Base DN')
	computer_class_name = Attribute('Computer Class Name', min_version='19.1')
	computer_query_expression = Attribute('Computer Query Expression', min_version='19.1')
	configuration = Attribute('Configuration')
	container_class_name = Attribute('Container Class Name')
	container_query_expression = Attribute('Container Query Expression')
	credential = Attribute('Credential')
	dsn = Attribute('DSN')
	distribution_list_class_name = Attribute('Distribution List Class Name')
	distribution_list_query_expression = Attribute('Distribution List Query Expression')
	friendly_name = Attribute('Friendly Name')
	group_class_name = Attribute('Group Class Name')
	group_query_expression = Attribute('Group Query Expression')
	host = Attribute('Host')
	no_rediscovery_on = Attribute('No Rediscovery On', min_version='21.2')
	port = Attribute('Port')
	resolve_nested_groups = Attribute('Resolve Nested Groups')
	search_filter = Attribute('Search Filter')
	search_root = Attribute('Search Root')
	secure = Attribute('Secure')
	timeout = Attribute('Timeout')
	user_class_name = Attribute('User Class Name')
	user_query_expression = Attribute('User Query Expression')
	vault_id = Attribute('Vault Id', min_version='18.2')
