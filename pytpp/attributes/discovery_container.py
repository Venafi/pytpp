from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class DiscoveryContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Discovery Container"
