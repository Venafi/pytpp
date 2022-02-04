from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportSSHDiscrepancyAttributes(ReportBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:SSH Discrepancy"
	options = Attribute('Options')
