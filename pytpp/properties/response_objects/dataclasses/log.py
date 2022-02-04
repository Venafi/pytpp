from datetime import datetime
from dataclasses import dataclass


@dataclass
class LogEvent:
    client_timestamp: datetime
    component: str
    component_id: int
    component_subsystem: str
    data: str
    grouping: int
    id: int
    name: str
    server_timestamp: datetime
    severity: str
    source_ip: str
    text1: str
    text2: str
    value1: int
    value2: int


@dataclass
class LogEventApplicationDefinition:
    application_name: str
    id: int


@dataclass
class LogEventDefinition:
    data_format: str
    data_title: str
    description: str
    grouping_title: str
    grouping_type: str
    id: int
    text1_title: str
    text2_title: str
    value1_title: str
    value1_type: str
    value2_title: str
    value2_type: str
