from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogHeartbeatAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    event = Attribute('Event')
    rule = Attribute('Rule')
    timeout = Attribute('Timeout')
