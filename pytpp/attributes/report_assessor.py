from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportAssessorAttributes(ReportBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:Assessor"
	jobdn = Attribute('JobDN')
	options = Attribute('Options')
