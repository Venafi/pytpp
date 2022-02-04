from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogApplicationAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Application"
	configuration = Attribute('Configuration')
	log_application_id = Attribute('Log Application ID')
	log_application_name = Attribute('Log Application Name')
	log_application_schema_en = Attribute('Log Application Schema EN')
