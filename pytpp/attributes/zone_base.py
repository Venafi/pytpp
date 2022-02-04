from pytpp.attributes._helper import IterableMeta, Attribute


class ZoneBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Zone Base"
	address_range = Attribute('Address Range')
	window_end = Attribute('Window End')
	window_start = Attribute('Window Start')
	zone_contact = Attribute('Zone Contact')
	zone_description = Attribute('Zone Description')
