from pytpp.properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses import metadata


class Metadata:
    @staticmethod
    def Result(code: int):
        return metadata.Result(
            code=code,
            metadata_result=ResultCodes.Metadata.get(code, 'Unknown'),
        )

    @staticmethod
    def Item(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return metadata.Item(
            allowed_characters=response_object.get('AllowedCharacters'),
            allowed_values=response_object.get('AllowedValues'),
            category=response_object.get('Category'),
            classes=response_object.get('Classes'),
            config_attribute=response_object.get('ConfigAttribute'),
            date_only=response_object.get('DateOnly'),
            default_values=response_object.get('DefaultValues'),
            display_after=response_object.get('DisplayAfter'),
            dn=response_object.get('DN'),
            error_message=response_object.get('ErrorMessage'),
            guid=response_object.get('Guid'),
            help=response_object.get('Help'),
            label=response_object.get('Label'),
            localization_table=response_object.get('LocalizationTable'),
            localized_help=response_object.get('LocalizedHelp'),
            localized_label=response_object.get('LocalizedLabel'),
            localized_set=response_object.get('LocalizedSet'),
            mandatory=response_object.get('Mandatory'),
            name=response_object.get('Name'),
            mask=response_object.get('Mask'),
            maximum_length=response_object.get('MaximumLength'),
            minimum_length=response_object.get('MinimumLength'),
            policyable=response_object.get('Policyable'),
            regular_expression=response_object.get('RegularExpression'),
            render_hidden=response_object.get('RenderHidden'),
            render_read_only=response_object.get('RenderReadOnly'),
            single=response_object.get('Single'),
            time_only=response_object.get('TimeOnly'),
            type=response_object.get('Type'),
        )

    @staticmethod
    def Data(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return metadata.Data(
            key=Metadata.Item(response_object.get('Key')),
            value=response_object.get('Value'),
        )

    @staticmethod
    def PolicyItem(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return metadata.PolicyItem(
            key=response_object.get('Key'),
            value=[Metadata.Item(value) for value in response_object.get('Value')],
        )
