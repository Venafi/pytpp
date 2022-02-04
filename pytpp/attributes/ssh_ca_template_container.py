from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class SSHCATemplateContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH CA Template Container"
