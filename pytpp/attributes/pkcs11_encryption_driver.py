from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.encryption_driver import EncryptionDriverAttributes


class Pkcs11EncryptionDriverAttributes(EncryptionDriverAttributes, metaclass=IterableMeta):
	__config_class__ = "Pkcs11 Encryption Driver"
	account_type = Attribute('Account Type')
	credential = Attribute('Credential')
	cryptokipath = Attribute('CryptokiPath')
	dsn = Attribute('DSN')
	default_key = Attribute('Default Key', min_version='18.1')
	encrypted_pin = Attribute('Encrypted Pin', min_version='18.1')
	fallback_pin = Attribute('Fallback Pin', min_version='21.2')
	key_generation = Attribute('Key Generation', min_version='18.1')
	key_storage = Attribute('Key Storage', min_version='19.2')
	key_validation = Attribute('Key Validation')
	permitted_keys = Attribute('Permitted Keys')
	slot_id = Attribute('Slot Id')
	token_label = Attribute('Token Label', min_version='20.4')
	token_serial = Attribute('Token Serial', min_version='20.4')
	verigram = Attribute('VeriGram', min_version='18.1')
