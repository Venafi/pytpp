from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class RiverbedSteelHeadAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Riverbed SteelHead"
	certificate_type = Attribute('Certificate Type', min_version='15.2')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.2')
	install_chain = Attribute('Install Chain', min_version='15.2')
	network_validation_disabled = Attribute('Network Validation Disabled', min_version='15.2')
	replace_existing = Attribute('Replace Existing', min_version='15.2')
