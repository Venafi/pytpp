from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CodeSigningApplicationAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Application"
	application_hash = Attribute('Application Hash', min_version='19.2')
	application_location = Attribute('Application Location', min_version='19.2')
	application_signatory_issuer = Attribute('Application Signatory Issuer', min_version='19.2')
	application_signatory_subject = Attribute('Application Signatory Subject', min_version='19.2')
	application_size = Attribute('Application Size', min_version='19.2')
	application_version = Attribute('Application Version', min_version='19.2')
	permitted_argument_pattern = Attribute('Permitted Argument Pattern', min_version='19.2')
	regular_expression = Attribute('Regular Expression', min_version='21.1')
	signing_object_file_argument_pattern = Attribute('Signing Object File Argument Pattern', min_version='19.2')
