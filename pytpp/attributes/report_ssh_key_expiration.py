from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes


class ReportSSHKeyExpirationAttributes(ReportBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:SSH Key Expiration"
	options = Attribute('Options')
