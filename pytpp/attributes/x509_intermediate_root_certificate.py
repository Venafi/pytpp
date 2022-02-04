from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.x509_root_certificate import X509RootCertificateAttributes


class X509IntermediateRootCertificateAttributes(X509RootCertificateAttributes, metaclass=IterableMeta):
	__config_class__ = "X509 Intermediate Root Certificate"
