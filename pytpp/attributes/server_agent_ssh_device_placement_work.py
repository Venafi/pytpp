from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.server_agent_base_device_placement_work import ServerAgentBaseDevicePlacementWorkAttributes


class ServerAgentSSHDevicePlacementWorkAttributes(ServerAgentBaseDevicePlacementWorkAttributes, metaclass=IterableMeta):
    __config_class__ = "Server Agent SSH Device Placement Work"
