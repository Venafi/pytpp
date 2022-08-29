from __future__ import annotations
from datetime import datetime
from pytpp.api.api_base import ObjectModel, ApiField


class LogEvent(ObjectModel):
    client_timestamp: datetime = ApiField(alias='ClientTimestamp')
    component: str = ApiField(alias='Component')
    component_id: int = ApiField(alias='ComponentId')
    component_subsystem: str = ApiField(alias='ComponentSubsystem')
    data: str = ApiField(alias='Data')
    grouping: int = ApiField(alias='Grouping')
    id: int = ApiField(alias='Id')
    name: str = ApiField(alias='Name')
    server_timestamp: datetime = ApiField(alias='ServerTimestamp')
    severity: str = ApiField(alias='Severity')
    source_ip: str = ApiField(alias='SourceIp')
    text1: str = ApiField(alias='Text1')
    text2: str = ApiField(alias='Text2')
    value1: int = ApiField(alias='Value1')
    value2: int = ApiField(alias='Value2')


class LogEventApplicationDefinition(ObjectModel):
    application_name: str = ApiField(alias='ApplicationName')
    id: int = ApiField(alias='Id')


class LogEventDefinition(ObjectModel):
    data_format: str = ApiField(alias='DataFormat')
    data_title: str = ApiField(alias='DataTitle')
    data_type: str = ApiField(alias='DataType')
    description: str = ApiField(alias='Description')
    grouping_title: str = ApiField(alias='GroupingTitle')
    grouping_type: str = ApiField(alias='GroupingType')
    id: int = ApiField(alias='Id')
    text1_title: str = ApiField(alias='Text1Title')
    text2_title: str = ApiField(alias='Text2Title')
    value1_title: str = ApiField(alias='Value1Title')
    value1_type: str = ApiField(alias='Value1Type')
    value2_title: str = ApiField(alias='Value2Title')
    value2_type: str = ApiField(alias='Value2Type')
