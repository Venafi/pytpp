from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.driver_base import DriverBaseAttributes


class CredentialDriverBaseAttributes(DriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Credential Driver Base"
