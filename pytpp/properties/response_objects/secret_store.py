from pytpp.properties.response_objects.dataclasses import secret_store
from pytpp.properties.resultcodes import ResultCodes


class SecretStore:
    @staticmethod
    def Result(code: int):
        return secret_store.Result(
            code=code,
            secret_store_result=ResultCodes.SecretStore.get(code, 'Unknown'),
        )

    @staticmethod
    def TypedNameValues(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return secret_store.TypedNameValues(
            name=response_object.get('Name'),
            type=response_object.get('Type'),
            value=response_object.get('Value'),
        )
