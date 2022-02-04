from dataclasses import dataclass


@dataclass
class Result:
    code: int
    config_result: str


@dataclass
class AttributeDefinition:
    name: str
    syntax: str


@dataclass
class ClassDefinition:
    containment_names: list
    containment_sub_names: list
    mandatory_names: list
    name: str
    naming_names: list
    optional_names: list
    super_class_names: list
