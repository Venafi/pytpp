from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ACMEOrderAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "ACME Order"
	acme_authorization_dn = Attribute('ACME Authorization DN', min_version='17.2')
	acme_expires = Attribute('ACME Expires', min_version='17.2')
	acme_not_after = Attribute('ACME Not After', min_version='17.2')
	acme_not_before = Attribute('ACME Not Before', min_version='17.2')
	csr_vault_id = Attribute('CSR Vault Id', min_version='17.2')
	certificate = Attribute('Certificate', min_version='17.2')
	error = Attribute('Error', min_version='17.2')
	identifier = Attribute('Identifier', min_version='21.2')
	status = Attribute('Status', min_version='17.2')
