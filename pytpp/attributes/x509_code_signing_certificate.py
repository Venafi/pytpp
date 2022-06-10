from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.x509_certificate import X509CertificateAttributes


class X509CodeSigningCertificateAttributes(X509CertificateAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    owner = Attribute('Owner', min_version='22.1')
