from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogChannelAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    configuration = Attribute('Configuration')
    driver_arguments = Attribute('Driver Arguments')
