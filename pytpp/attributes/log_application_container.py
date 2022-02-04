from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class LogApplicationContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Log Application Container"
