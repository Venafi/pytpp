from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class CodeSigningActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Action"
