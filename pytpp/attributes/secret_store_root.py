from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class SecretStoreRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Secret Store Root"
	certificate_protection_key = Attribute('Certificate Protection Key')
	dsn = Attribute('DSN')
	driver_name = Attribute('Driver Name')
	non_authoritative_classes = Attribute('Non-Authoritative Classes', min_version='21.1')
	pkcs8_association = Attribute('PKCS8 Association')
	x509certificate_association = Attribute('X509Certificate Association')
