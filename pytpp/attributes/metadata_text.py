from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataTextAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Metadata Text"
	allowed_characters = Attribute('Allowed Characters')
	error_message = Attribute('Error Message')
	mask = Attribute('Mask')
	maximum_length = Attribute('Maximum Length')
	minimum_length = Attribute('Minimum Length')
	regular_expression = Attribute('Regular Expression')
