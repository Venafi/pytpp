from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class FlowActionAddTeamMemberAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
