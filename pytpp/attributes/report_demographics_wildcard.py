from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportDemographicsWildcardAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:Demographics Wildcard"
