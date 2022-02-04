from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class ClientGroupContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Group Container"
