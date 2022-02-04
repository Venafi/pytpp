from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportClientsAttributes(ReportBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:Clients"
