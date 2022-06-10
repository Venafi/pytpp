from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class UniCERTCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    ca_dn = Attribute('CA DN')
    ra_dn = Attribute('RA DN')
    secure = Attribute('Secure')
    web_instance = Attribute('Web Instance')
