from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class CodeSigningProjectRootAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Project Root"
