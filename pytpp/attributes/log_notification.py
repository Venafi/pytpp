from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogNotificationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    log_channel = Attribute('Log Channel')
    rule = Attribute('Rule')
