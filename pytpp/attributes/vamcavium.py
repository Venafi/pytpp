from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class VamCaviumAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "VamCavium"
	cavium_utility_path = Attribute('Cavium Utility Path')
	key_list_path = Attribute('Key List Path')
