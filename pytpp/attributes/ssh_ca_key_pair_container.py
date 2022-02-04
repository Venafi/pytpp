from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class SSHCAKeyPairContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH CA Key Pair Container"
