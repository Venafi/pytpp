from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.identity_driver import IdentityDriverAttributes


class LDAPIdentityDriverAttributes(IdentityDriverAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    ambiguous_name_resolution = Attribute('Ambiguous Name Resolution')
    base_dn = Attribute('Base DN')
    configuration = Attribute('Configuration')
    connection_timeout = Attribute('Connection Timeout')
    container_class_name = Attribute('Container Class Name')
    container_query_expression = Attribute('Container Query Expression')
    dsn = Attribute('DSN')
    friendly_name = Attribute('Friendly Name')
    group_class_name = Attribute('Group Class Name')
    group_query_expression = Attribute('Group Query Expression')
    group_search_root = Attribute('Group Search Root')
    host = Attribute('Host')
    internal_identifier = Attribute('Internal Identifier')
    login_name_resolution = Attribute('Login Name Resolution')
    member_identifier = Attribute('Member Identifier')
    memberof_enabled = Attribute('MemberOf Enabled', min_version='15.2')
    membership_resolution = Attribute('Membership Resolution', min_version='15.2')
    port = Attribute('Port')
    resolve_nested_groups = Attribute('Resolve Nested Groups')
    revocation = Attribute('Revocation')
    search_root = Attribute('Search Root')
    secure = Attribute('Secure')
    size_limit = Attribute('Size Limit')
    timeout = Attribute('Timeout')
    title = Attribute('Title')
    universal_identifier = Attribute('Universal Identifier')
    user_class_name = Attribute('User Class Name')
    user_query_expression = Attribute('User Query Expression')
    vault_id = Attribute('Vault Id', min_version='18.2')
    vendor = Attribute('Vendor')
