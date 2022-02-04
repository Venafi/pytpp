from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class FlowActionApproverBaseAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Flow Action Approver Base"
	minimum_approvers = Attribute('Minimum Approvers', min_version='19.2')
