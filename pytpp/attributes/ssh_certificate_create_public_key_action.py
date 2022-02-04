from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class SSHCertificateCreatePublicKeyActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Certificate Create Public Key Action"
