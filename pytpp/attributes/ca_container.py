from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class CAContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "CA Container"
