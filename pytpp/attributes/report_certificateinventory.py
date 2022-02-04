from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCertificateInventoryAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:CertificateInventory"
	grouping = Attribute('Grouping')
	options = Attribute('Options')
	policydn = Attribute('PolicyDN')
