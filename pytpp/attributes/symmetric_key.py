from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.legacy_key_base import LegacyKeyBaseAttributes
from pytpp.attributes.monitoring_base import MonitoringBaseAttributes
from pytpp.attributes.top import TopAttributes


class SymmetricKeyAttributes(LegacyKeyBaseAttributes, MonitoringBaseAttributes, TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Symmetric Key"
	check_value = Attribute('Check Value')
