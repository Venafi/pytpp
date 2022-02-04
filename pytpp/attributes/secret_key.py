from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.key_base import KeyBaseAttributes


class SecretKeyAttributes(KeyBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Secret Key"
	secret_key_renewal_flow = Attribute('Secret Key Renewal Flow', min_version='20.2')
