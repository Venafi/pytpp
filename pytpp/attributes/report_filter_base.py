from pytpp.attributes._helper import IterableMeta, Attribute


class ReportFilterBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Report Filter Base"
	address = Attribute('Address')
	discoverydn = Attribute('DiscoveryDN')
	grouping = Attribute('Grouping')
	longrunning = Attribute('LongRunning', min_version='16.4')
	policydn = Attribute('PolicyDN')
	reporton = Attribute('ReportOn')
	selectedcontacts = Attribute('SelectedContacts')
