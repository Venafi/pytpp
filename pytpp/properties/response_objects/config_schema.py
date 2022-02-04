from pytpp.properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses import config_schema


class ConfigSchema:
    @staticmethod
    def Result(code: int):
        return config_schema.Result(
            code=code,
            config_result=ResultCodes.Config.get(code, 'Unknown'),
        )

    @staticmethod
    def AttributeDefinition(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return config_schema.AttributeDefinition(
            name=response_object.get('Name'),
            syntax=response_object.get('Syntax'),
        )

    @staticmethod
    def ClassDefinition(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return config_schema.ClassDefinition(
            containment_names=response_object.get('ContainmentNames'),
            containment_sub_names=response_object.get('ContainmentSubNames'),
            mandatory_names=response_object.get('MandatoryNames'),
            name=response_object.get('Name'),
            naming_names=response_object.get('NamingNames'),
            optional_names=response_object.get('OptionalNames'),
            super_class_names=response_object.get('SuperClassNames'),
        )
