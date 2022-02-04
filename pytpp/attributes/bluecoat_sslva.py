from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class BlueCoatSSLVAAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "BlueCoat SSLVA"
	certificate_label = Attribute('Certificate Label')
	certificate_oid = Attribute('Certificate OID')
	certificate_only = Attribute('Certificate Only')
	create_lists = Attribute('Create Lists')
	device_certificate = Attribute('Device Certificate')
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	replace_store = Attribute('Replace Store')
