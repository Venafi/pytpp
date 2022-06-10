from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class CodeSigningApplicationContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
