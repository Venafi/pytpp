# noinspection PyUnresolvedReferences
from pytpp._about import (
    __version__, __author__, __author_email__, __project_name__,
    __project_url__,
)
# noinspection PyUnresolvedReferences
from pytpp.api.authenticate import Authenticate
# noinspection PyUnresolvedReferences
from pytpp.api.websdk.enums.oauth import Scope
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.features import Features
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attributes import Attributes
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attribute_values import AttributeValues
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.classes import Classes as ClassNames
# noinspection PyUnresolvedReferences
from pytpp.tools.logger import logger, features_logger, api_logger
# noinspection ALL
from pytpp.tools import vtypes as Types
from pytpp.api.websdk import models, enums


def __getattr__(name):
    if name == 'AttributeNames':
        raise ImportError('Importing AttributeNames has been deprecated since PyTPP 2.0. Use "Attributes" instead.')
    elif name == 'Classes':
        raise ImportError('Importing Classes has been deprecated since PyTPP 2.0. Use "ClassNames" instead.')
    raise ImportError(f'{name} cannot be imported because it does not exist.')
