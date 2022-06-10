from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.code_signing_environment_base import CodeSigningEnvironmentBaseAttributes


class CodeSigningAppleEnvironmentAttributes(CodeSigningEnvironmentBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Apple Environment"
    cn_pattern = Attribute('CN Pattern', min_version='21.2')
    certificate_authority = Attribute('Certificate Authority', min_version='22.1')
    certificate_dn = Attribute('Certificate DN', min_version='21.2')
    city = Attribute('City', min_version='22.1')
    country = Attribute('Country', min_version='22.1')
    elliptic_curve = Attribute('Elliptic Curve', min_version='22.1')
    key_algorithm = Attribute('Key Algorithm', min_version='22.1')
    key_bit_strength = Attribute('Key Bit Strength', min_version='22.1')
    key_storage_location = Attribute('Key Storage Location', min_version='21.2')
    organization = Attribute('Organization', min_version='22.1')
    organizational_unit = Attribute('Organizational Unit', min_version='22.1')
    state = Attribute('State', min_version='22.1')
    x509_subject = Attribute('X509 Subject', min_version='22.1')
