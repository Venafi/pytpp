from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.x509_certificate import X509CertificateAttributes


class X509TimeStampingCertificateAttributes(X509CertificateAttributes, metaclass=IterableMeta):
	__config_class__ = "X509 Time Stamping Certificate"
