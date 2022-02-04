from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes


class ReportBaseAttributes(DriverBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Report Base"
	csv_vault_id = Attribute('CSV Vault Id')
	configuration = Attribute('Configuration')
	creation_date = Attribute('Creation Date')
	credential = Attribute('Credential')
	delivery_type = Attribute('Delivery Type')
	format = Attribute('Format')
	html_vault_id = Attribute('HTML Vault Id')
	internet_email_address = Attribute('Internet EMail Address')
	last_run = Attribute('Last Run')
	options = Attribute('Options')
	pdf_vault_id = Attribute('PDF Vault Id')
	publishing_host = Attribute('Publishing Host')
	publishing_location = Attribute('Publishing Location')
	rtf_vault_id = Attribute('RTF Vault Id')
	report_template = Attribute('Report Template')
	skip_empty = Attribute('Skip Empty')
	title = Attribute('Title')
	xml_vault_id = Attribute('XML Vault Id')
