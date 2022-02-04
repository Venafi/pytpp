from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Engine:
    dn: str
    display_name: str
    guid: str
    id: int
    name: str


@dataclass
class Services:
    vplatform: 'Service'
    log_server: 'Service'
    iis: 'Service'


@dataclass
class Service:
    modules: list
    time_since_first_seen: datetime
    time_since_last_seen: datetime
    status: str


@dataclass
class SystemStatus:
    engine_name: str
    services: 'Services'
    version: str


@dataclass
class Task:
    display_name: str
    name: str
    start_time: datetime
    stop_time: datetime
    warning_count: int


@dataclass
class UpgradeInfo:
    id: str
    start_time: datetime
    versions: List[str]


@dataclass
class UpgradeStatus:
    engine: 'Engine'
    status: str
    upgrade_start_time: datetime
    upgrade_stop_time: datetime
    tasks_completed: 'List[Task]'
    tasks_pending: 'List[Task]'
    tasks_running: 'List[Task]'


@dataclass
class UpgradeSummary:
    status: str
    upgrade_start_time: datetime
    upgrade_stop_time: datetime
    completed_tasks: int
    target_version: str
    engines_complete: int
    engines_running: int
    engines_blocked: int
    engines_in_error: int
    engines_pending_install: int
