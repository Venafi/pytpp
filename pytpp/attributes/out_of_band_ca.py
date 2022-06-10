from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class OutOfBandCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Out Of Band CA"
    email_contacts = Attribute('Email Contacts', min_version='22.1')
    internet_email_address = Attribute('Internet EMail Address', min_version='22.1')
