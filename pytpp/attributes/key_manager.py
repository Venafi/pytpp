from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.service_module import ServiceModuleAttributes


class KeyManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Key Manager"
