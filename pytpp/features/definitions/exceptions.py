from pytpp.tools.logger import features_logger


class FeatureException(Exception):
    def log(self):
        features_logger.error(self.__str__(), stacklevel=2)


class InvalidFormat(FeatureException): ...


class InvalidResultCode(FeatureException):
    def __init__(self, code: int, code_description: str = 'Unknown'):
        super().__init__(f'Expected a valid result code, but got "{code}": {code_description}.')


class ObjectDoesNotExist(FeatureException): ...


class UnexpectedValue(FeatureException): ...
