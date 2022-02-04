from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.service_module import ServiceModuleAttributes


class OnboardDiscoveryManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Onboard Discovery Manager"
