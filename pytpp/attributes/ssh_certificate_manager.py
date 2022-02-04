from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.service_module import ServiceModuleAttributes


class SSHCertificateManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Certificate Manager"
