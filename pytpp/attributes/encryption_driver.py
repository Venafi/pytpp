from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class EncryptionDriverAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    encryption_data = Attribute('Encryption Data')
