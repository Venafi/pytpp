from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LicenseAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "License"
	license_key = Attribute('License Key')
