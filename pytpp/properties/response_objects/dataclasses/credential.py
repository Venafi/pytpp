from dataclasses import dataclass


@dataclass
class Result:
    code: int
    credential_result: str


@dataclass
class CredentialInfo:
    class_name: str
    full_name: str


@dataclass
class NameTypeValue:
    name: str
    type: str
    value: str
