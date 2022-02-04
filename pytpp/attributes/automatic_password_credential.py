from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class AutomaticPasswordCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Automatic Password Credential"
	self_destruct = Attribute('Self Destruct')
	usage_count = Attribute('Usage Count')
