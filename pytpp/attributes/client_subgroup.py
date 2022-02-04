from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.client_group_base import ClientGroupBaseAttributes


class ClientSubgroupAttributes(ClientGroupBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Subgroup"
