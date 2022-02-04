from pytpp.properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses import config


class Config:
    @staticmethod
    def Result(code: int):
        return config.Result(
            code=code,
            config_result=ResultCodes.Config.get(code, 'Unknown')
        )

    @staticmethod
    def NameValues(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return config.NameValues(
            name=response_object.get('Name'),
            values=response_object.get('Values'),
        )

    @staticmethod
    def Object(response_object: dict):
        """
        See Also:
            See :ref:`config_object` and :ref:`dn` for more information.
        """
        if not isinstance(response_object, dict):
            response_object = {}
        return config.Object(
            absolute_guid=response_object.get('AbsoluteGUID'),
            dn=response_object.get('DN'),
            guid=response_object.get('GUID'),
            config_id=response_object.get('Id'),
            name=response_object.get('Name'),
            parent=response_object.get('Parent'),
            revision=response_object.get('Revision'),
            type_name=response_object.get('TypeName'),
        )

    @staticmethod
    def Policy(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return config.Policy(
            attribute_name=response_object.get('AttributeName'),
            guid=response_object.get('GUID'),
            property=response_object.get('Property'),
            type_name=response_object.get('TypeName'),
            value_list=response_object.get('ValueList'),
        )
