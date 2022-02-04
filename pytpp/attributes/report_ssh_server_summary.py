from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportSSHServerSummaryAttributes(ReportBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:SSH Server Summary"
	options = Attribute('Options')
