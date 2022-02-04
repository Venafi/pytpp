from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class IIS5Attributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "IIS5"
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	site_id = Attribute('Site Id')
