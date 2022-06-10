from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class PrivateKeyCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    username = Attribute('Username')
