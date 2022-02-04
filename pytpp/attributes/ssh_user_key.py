from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.ssh_key import SSHKeyAttributes


class SSHUserKeyAttributes(SSHKeyAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH User Key"
