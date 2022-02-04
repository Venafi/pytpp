from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class ClientWorkRootAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Work Root"
