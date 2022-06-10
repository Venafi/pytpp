from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class OAuthDeviceAuthorizationWaitForIdentityActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "OAuth Device Authorization Wait For Identity Action"
