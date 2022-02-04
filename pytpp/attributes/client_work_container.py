from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class ClientWorkContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Work Container"
