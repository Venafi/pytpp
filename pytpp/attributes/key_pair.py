from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.key_base import KeyBaseAttributes


class KeyPairAttributes(KeyBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Key Pair"
	created_by = Attribute('Created By', min_version='20.3')
	gpg_public_key_vault_id = Attribute('GPG Public Key Vault ID', min_version='21.4')
	key_pair_renewal_flow = Attribute('Key Pair Renewal Flow', min_version='20.2')
	original_creation_date = Attribute('Original Creation Date', min_version='20.2')
	public_key_vault_id = Attribute('Public Key Vault Id', min_version='20.2')
