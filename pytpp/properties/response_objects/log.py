from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.properties.response_objects.dataclasses import log


class Log:
    @staticmethod
    def LogEvent(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return log.LogEvent(
            client_timestamp=from_date_string(response_object.get('ClientTimestamp')),
            component=response_object.get('Component'),
            component_id=response_object.get('ComponentId'),
            component_subsystem=response_object.get('ComponentSubsystem'),
            data=response_object.get('Data'),
            grouping=response_object.get('Grouping'),
            id=response_object.get('Id'),
            name=response_object.get('Name'),
            server_timestamp=from_date_string(response_object.get('ServerTimestamp')),
            severity=response_object.get('Severity'),
            source_ip=response_object.get('SourceIP'),
            text1=response_object.get('Text1'),
            text2=response_object.get('Text2'),
            value1=response_object.get('Value1'),
            value2=response_object.get('Value2'),
        )

    @staticmethod
    def LogEventApplicationDefinition(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return log.LogEventApplicationDefinition(
            application_name=response_object.get('ApplicationName'),
            id=response_object.get('ID'),
        )

    @staticmethod
    def LogEventDefinition(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return log.LogEventDefinition(
            data_format=response_object.get('DataFormat'),
            data_title=response_object.get('DataTitle'),
            description=response_object.get('Description'),
            grouping_title=response_object.get('GroupingTitle'),
            grouping_type=response_object.get('GroupingType'),
            id=response_object.get('ID'),
            text1_title=response_object.get('Text1Title'),
            text2_title=response_object.get('Text2Title'),
            value1_title=response_object.get('Value1Title'),
            value1_type=response_object.get('Value1Type'),
            value2_title=response_object.get('Value2Title'),
            value2_type=response_object.get('Value2Type'),
        )
