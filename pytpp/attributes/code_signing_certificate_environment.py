from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes


class CodeSigningCertificateEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Certificate Environment"
	ca_specific_attributes = Attribute('CA Specific Attributes', min_version='21.3')
	certificate_authority = Attribute('Certificate Authority', min_version='20.3')
	certificate_dn = Attribute('Certificate DN', min_version='20.1')
	city = Attribute('City', min_version='20.3')
	country = Attribute('Country', min_version='20.3')
	elliptic_curve = Attribute('Elliptic Curve', min_version='20.3')
	key_algorithm = Attribute('Key Algorithm', min_version='20.3')
	key_bit_strength = Attribute('Key Bit Strength', min_version='20.3')
	key_storage_location = Attribute('Key Storage Location', min_version='20.3')
	organization = Attribute('Organization', min_version='20.3')
	organizational_unit = Attribute('Organizational Unit', min_version='20.3')
	provide_chain = Attribute('Provide Chain', min_version='20.2')
	state = Attribute('State', min_version='20.3')
	synchronize_chain = Attribute('Synchronize Chain')
	target_store = Attribute('Target Store', min_version='20.4')
	x509_subject = Attribute('X509 Subject', min_version='20.3')
	x509_subjectaltname_rfc822 = Attribute('X509 SubjectAltName RFC822', min_version='20.3')
