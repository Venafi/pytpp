from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataListAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Metadata List"
	single = Attribute('Single')
