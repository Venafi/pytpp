from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_group_base import ClientGroupBaseAttributes


class ClientGroupAttributes(ClientGroupBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Group"
	agent_type = Attribute('Agent Type', min_version='15.2')
