from dataclasses import dataclass


@dataclass
class Result:
    code: int
    secret_store_result: str


@dataclass
class TypedNameValues:
    name: str
    type: str
    value: str
