from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class SSHAutomaticRotationTriggerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Automatic Rotation Trigger"
