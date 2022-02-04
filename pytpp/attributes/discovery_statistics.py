from pytpp.attributes._helper import IterableMeta, Attribute


class DiscoveryStatisticsAttributes(metaclass=IterableMeta):
	__config_class__ = "Discovery Statistics"
	certificates_found = Attribute('Certificates Found')
	completed_scans = Attribute('Completed Scans')
	connect_succeeded = Attribute('Connect Succeeded')
	keys_found = Attribute('Keys Found')
