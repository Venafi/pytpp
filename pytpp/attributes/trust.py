from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class TrustAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Trust"
	allow_from = Attribute('Allow From', min_version='19.3')
	allowed_algorithm = Attribute('Allowed Algorithm', min_version='19.3')
	allowed_command = Attribute('Allowed Command', min_version='19.3')
	allowed_vendor_types = Attribute('Allowed Vendor Types', min_version='19.3')
	contact = Attribute('Contact', min_version='19.3')
	deny_from = Attribute('Deny From', min_version='19.3')
	key_bit_strength = Attribute('Key Bit Strength', min_version='19.3')
	maximum_authorizations_per_keyset = Attribute('Maximum Authorizations Per Keyset', min_version='20.1')
	minimum_key_bit_strength = Attribute('Minimum Key Bit Strength', min_version='19.3')
	required_options = Attribute('Required Options', min_version='19.3')
	trust_id = Attribute('Trust Id', min_version='19.3')
