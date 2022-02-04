from pytpp.properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses import credential


class Credential:
    @staticmethod
    def Result(code: int):
        return credential.Result(
            code=code,
            credential_result=ResultCodes.Credential.get(code, 'Unknown'),
        )

    @staticmethod
    def CredentialInfo(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return credential.CredentialInfo(
            class_name=response_object.get('ClassName'),
            full_name=response_object.get('FullName'),
        )

    @staticmethod
    def NameTypeValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return credential.NameTypeValue(
            name=response_object.get('Name'),
            type=response_object.get('Type'),
            value=response_object.get('Value'),
        )
