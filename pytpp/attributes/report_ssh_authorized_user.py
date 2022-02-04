from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportSSHAuthorizedUserAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:SSH Authorized User"
	options = Attribute('Options')
