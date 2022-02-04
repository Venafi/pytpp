from packaging.version import Version
from typing import List, Generator


class Attribute(str):
    def __init__(self, name: str, min_version: str = None):
        self.name = name
        self.min_version = min_version
        if min_version is not None:
            self.min_version = Version('.'.join(self.min_version.split('.', maxsplit=2)[:2]))

    def __new__(cls, name: str, *args, **kwargs):
        return str().__new__(cls, name)


class IterableMeta(type):
    __config_class__ = None

    def __iter__(self) -> Generator[Attribute, None, None]:
        for item in dir(self):
            if not item.startswith('_'):
                attr = getattr(self, item)
                if not callable(attr):
                    yield attr

    def list(cls) -> List[Attribute]:
        return list(iter(cls))  # type: List[Attribute]

    def __repr__(self):
        return self.__config_class__

    def __str__(self):
        return self.__config_class__
