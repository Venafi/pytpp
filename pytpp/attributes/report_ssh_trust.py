from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportSSHTrustAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    options = Attribute('Options')
