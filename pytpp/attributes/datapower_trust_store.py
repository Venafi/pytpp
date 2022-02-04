from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes


class DataPowerTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "DataPower Trust Store"
	application_domain = Attribute('Application Domain', min_version='20.3')
	crl_distribution_points_handling = Attribute('CRL Distribution Points Handling', min_version='20.3')
	certificate_validation_mode = Attribute('Certificate Validation Mode', min_version='20.3')
	check_dates = Attribute('Check Dates', min_version='20.3')
	crypto_validation_credential_name = Attribute('Crypto Validation Credential Name', min_version='20.3')
	folder = Attribute('Folder', min_version='20.3')
	maximum_length = Attribute('Maximum Length', min_version='20.3')
	require_crl = Attribute('Require CRL', min_version='20.3')
	use_crl = Attribute('Use CRL', min_version='20.3')
