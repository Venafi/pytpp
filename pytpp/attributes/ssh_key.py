from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.agent_base import AgentBaseAttributes
from pytpp.attributes.driver_base import DriverBaseAttributes
from pytpp.attributes.legacy_key_base import LegacyKeyBaseAttributes
from pytpp.attributes.monitoring_base import MonitoringBaseAttributes


class SSHKeyAttributes(AgentBaseAttributes, DriverBaseAttributes, LegacyKeyBaseAttributes, MonitoringBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Key"
	public_key_vault_id = Attribute('Public Key Vault Id')
