from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.organization import OrganizationAttributes


class IdentityRootAttributes(OrganizationAttributes, metaclass=IterableMeta):
	__config_class__ = "Identity Root"
	authentication_scheme = Attribute('Authentication Scheme')
	identity_cache_timeout = Attribute('Identity Cache Timeout', min_version='16.2')
