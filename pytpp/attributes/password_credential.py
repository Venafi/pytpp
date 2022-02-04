from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.credential_base import CredentialBaseAttributes


class PasswordCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Password Credential"
