from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.encryption_driver import EncryptionDriverAttributes


class DPAPIEncryptionDriverAttributes(EncryptionDriverAttributes, metaclass=IterableMeta):
	__config_class__ = "DPAPI Encryption Driver"
	generation_only = Attribute('Generation Only', min_version='18.1')
	key_validation = Attribute('Key Validation')
	verigram = Attribute('VeriGram', min_version='18.1')
