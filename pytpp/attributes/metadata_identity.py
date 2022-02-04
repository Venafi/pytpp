from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataIdentityAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Metadata Identity"
	single = Attribute('Single')
