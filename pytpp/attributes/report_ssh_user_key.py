from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportSSHUserKeyAttributes(ReportBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:SSH User Key"
	options = Attribute('Options')
