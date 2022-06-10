from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class FlowActionBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    rank = Attribute('Rank', min_version='19.2')
