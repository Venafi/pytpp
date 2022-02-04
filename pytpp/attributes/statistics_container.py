from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class StatisticsContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Statistics Container"
