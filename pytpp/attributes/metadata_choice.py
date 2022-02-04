from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataChoiceAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Metadata Choice"
	single = Attribute('Single')
