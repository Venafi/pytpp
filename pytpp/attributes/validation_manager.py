from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.service_module import ServiceModuleAttributes


class ValidationManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    start_time = Attribute('Start Time')
