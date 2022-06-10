from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class CodeSignPreApprovalActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    stage_identifier = Attribute('Stage Identifier', min_version='20.2')
