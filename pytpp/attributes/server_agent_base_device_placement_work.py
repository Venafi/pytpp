from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes


class ServerAgentBaseDevicePlacementWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Server Agent Base Device Placement Work"
	device_object_location = Attribute('Device Object Location', min_version='20.1')
	device_share_mode = Attribute('Device Share Mode', min_version='20.1')
