from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class TealeafPCAAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Tealeaf PCA"
	file_validation_disabled = Attribute('File Validation Disabled')
	install_path = Attribute('Install Path')
