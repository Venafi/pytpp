from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ClientWorkBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    work_guid = Attribute('Work Guid')
