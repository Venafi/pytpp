from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCertificateNetworkValidationAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:CertificateNetworkValidation"
	certificateslimit = Attribute('CertificatesLimit')
	grouping = Attribute('Grouping')
	options = Attribute('Options')
	policydn = Attribute('PolicyDN')
