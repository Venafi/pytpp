from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class F5AuthenticationBundleAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "F5 Authentication Bundle"
	advanced_settings_bundle_name = Attribute('Advanced Settings Bundle Name')
	certificates = Attribute('Certificates')
