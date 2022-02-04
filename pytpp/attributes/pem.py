from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class PEMAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "PEM"
	certificate_chain_file = Attribute('Certificate Chain File')
	certificate_file = Attribute('Certificate File')
	file_validation_disabled = Attribute('File Validation Disabled')
	network_validation_disabled = Attribute('Network Validation Disabled')
	overwrite_existing_chain = Attribute('Overwrite Existing Chain')
	pbes2_algorithm = Attribute('PBES2 Algorithm')
	private_key_file = Attribute('Private Key File')
