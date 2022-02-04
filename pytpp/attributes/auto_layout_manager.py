from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.service_module import ServiceModuleAttributes


class AutoLayoutManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Auto Layout Manager"
