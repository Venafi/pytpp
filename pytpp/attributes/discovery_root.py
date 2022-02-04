from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class DiscoveryRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Discovery Root"
	address_range = Attribute('Address Range')
	dsn = Attribute('DSN')
	driver_name = Attribute('Driver Name')
	protection_key = Attribute('Protection Key')
	timeout = Attribute('Timeout')
