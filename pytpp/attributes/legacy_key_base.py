from pytpp.attributes._helper import IterableMeta, Attribute


class LegacyKeyBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Legacy Key Base"
	algorithm = Attribute('Algorithm')
	approver = Attribute('Approver')
	key_bit_strength = Attribute('Key Bit Strength')
	key_vault_id = Attribute('Key Vault Id')
	protection_key = Attribute('Protection Key')
