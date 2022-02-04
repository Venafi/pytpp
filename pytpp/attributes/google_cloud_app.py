from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class GoogleCloudAppAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Google Cloud App"
	file_validation_disabled = Attribute('File Validation Disabled', min_version='20.2')
	network_validation_disabled = Attribute('Network Validation Disabled', min_version='20.2')
	target_proxy_name = Attribute('Target Proxy Name', min_version='20.2')
	target_proxy_type = Attribute('Target Proxy Type', min_version='20.2')
	target_region = Attribute('Target Region', min_version='21.4')
	target_resource = Attribute('Target Resource', min_version='20.2')
	timeout = Attribute('Timeout', min_version='20.2')
