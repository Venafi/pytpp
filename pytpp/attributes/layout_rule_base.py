from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LayoutRuleBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    rule = Attribute('Rule', min_version='19.1')
    vault_id = Attribute('Vault Id')
