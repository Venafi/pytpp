from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogNotificationContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    description = Attribute('Description')
