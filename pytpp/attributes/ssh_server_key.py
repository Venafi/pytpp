from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.ssh_key import SSHKeyAttributes
from pytpp.attributes.validation_base import ValidationBaseAttributes


class SSHServerKeyAttributes(SSHKeyAttributes, ValidationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Server Key"
	network_validation_disabled = Attribute('Network Validation Disabled')
