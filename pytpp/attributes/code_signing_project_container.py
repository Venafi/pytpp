from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class CodeSigningProjectContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Project Container"
