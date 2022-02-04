from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class CodeSigningEnvironmentRootAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Environment Root"
