# noinspection PyUnresolvedReferences
from pytpp._about import (
    __version__, __author__, __author_email__, __project_name__,
    __project_url__,
)
# noinspection PyUnresolvedReferences
from pytpp.api.authenticate import Authenticate
# noinspection PyUnresolvedReferences
from pytpp.properties.oauth import Scope
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.features import Features
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attributes import Attributes
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attribute_values import AttributeValues
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.classes import Classes as ClassNames
# noinspection PyUnresolvedReferences
from pytpp.tools.logger import logger
# noinspection PyUnresolvedReferences
from pytpp.tools import vtypes as Types
# Legacy imports
from pytpp.features.definitions.legacy_attribute_names import AttributeNames as __AN
from pytpp.features.definitions.legacy_classes import Classes as __C

def __getattr__(name):
    if name == 'AttributeNames':
        return __AN
    elif name == 'Classes':
        return __C
    raise ImportError(f'{name} cannot be imported because it does not exist.')

