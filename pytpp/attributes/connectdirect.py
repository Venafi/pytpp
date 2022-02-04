from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class ConnectDirectAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "ConnectDirect"
	certificate_label = Attribute('Certificate Label')
	certificate_only = Attribute('Certificate Only')
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	node_name = Attribute('Node Name')
	protocol = Attribute('Protocol')
