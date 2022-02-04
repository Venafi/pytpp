from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ACMEAccountAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "ACME Account"
	account_key_hash = Attribute('Account Key Hash', min_version='17.2')
	certificate_location_dn = Attribute('Certificate Location DN', min_version='17.2')
	internet_email_address = Attribute('Internet EMail Address', min_version='17.2')
	json_web_key = Attribute('JSON Web Key', min_version='21.2')
	public_key_vault_id = Attribute('Public Key Vault Id', min_version='17.2')
	status = Attribute('Status', min_version='17.2')
