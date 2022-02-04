from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class DriverBaseAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Driver Base"
	driver_arguments = Attribute('Driver Arguments')
	driver_name = Attribute('Driver Name')
	rank = Attribute('Rank')
