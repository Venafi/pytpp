from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCustomReportAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report:Custom Report"
	custom_report_data_type = Attribute('Custom Report: Data Type', min_version='15.3')
	custom_report_entity_type = Attribute('Custom Report: Entity Type', min_version='19.2')
	custom_report_filter = Attribute('Custom Report: Filter', min_version='15.3')
	custom_report_order_by = Attribute('Custom Report: Order By', min_version='15.3')
	custom_report_owner = Attribute('Custom Report: Owner', min_version='16.1')
	custom_report_personalized = Attribute('Custom Report: Personalized', min_version='15.3')
	custom_report_selected_field = Attribute('Custom Report: Selected Field', min_version='15.3')
	custom_report_sort_descending = Attribute('Custom Report: Sort Descending', min_version='15.3')
	error_message = Attribute('Error Message', min_version='15.3')
	options = Attribute('Options', min_version='15.3')
	status = Attribute('Status', min_version='15.3')
	summary = Attribute('Summary', min_version='15.3')
