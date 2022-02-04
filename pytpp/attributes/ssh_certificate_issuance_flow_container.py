from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class SSHCertificateIssuanceFlowContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Certificate Issuance Flow Container"
