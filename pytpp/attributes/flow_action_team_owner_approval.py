from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.flow_action_config_read_approvers import FlowActionConfigReadApproversAttributes


class FlowActionTeamOwnerApprovalAttributes(FlowActionConfigReadApproversAttributes, metaclass=IterableMeta):
	__config_class__ = "Flow Action Team Owner Approval"
