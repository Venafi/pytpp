from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class RemoteAccessApplicationContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Remote Access Application Container"
