from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ExclusionAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    rule = Attribute('Rule')
