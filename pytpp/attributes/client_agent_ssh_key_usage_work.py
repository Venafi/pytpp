from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_agent_ssh_provisioning_work import ClientAgentSSHProvisioningWorkAttributes


class ClientAgentSSHKeyUsageWorkAttributes(ClientAgentSSHProvisioningWorkAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Agent SSH Key Usage Work"
	max_row_count = Attribute('Max Row Count')
