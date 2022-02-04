from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class BasicAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Basic"
	certificate_file = Attribute('Certificate File', min_version='15.2')
	network_validation_disabled = Attribute('Network Validation Disabled')
