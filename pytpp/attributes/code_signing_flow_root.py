from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class CodeSigningFlowRootAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Flow Root"
