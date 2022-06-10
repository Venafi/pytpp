from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.flow_action_approver_base import FlowActionApproverBaseAttributes


class FlowActionDirectApproversAttributes(FlowActionApproverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    direct_approver = Attribute('Direct Approver', min_version='19.2')
