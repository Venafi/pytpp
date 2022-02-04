from pytpp.properties.response_objects.dataclasses import system_status
from pytpp.tools.helpers.date_converter import from_date_string


class SystemStatus:
    @staticmethod
    def Engine(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return system_status.Engine(
            dn=response_object.get('DN'),
            display_name=response_object.get('DisplayName'),
            guid=response_object.get('Guid'),
            id=response_object.get('Id'),
            name=response_object.get('Name'),
        )

    @staticmethod
    def Services(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        return system_status.Services(
            vplatform=SystemStatus.Service(response_object.get('vPlatform')),
            log_server=SystemStatus.Service(response_object.get('logServer')),
            iis=SystemStatus.Service(response_object.get('iis')),
        )

    @staticmethod
    def Service(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        return system_status.Service(
            modules=response_object.get('modules'),
            time_since_first_seen=from_date_string(response_object.get('timeSinceFirstSeen'), duration_format=True),
            time_since_last_seen=from_date_string(response_object.get('timeSinceLastSeen'), duration_format=True),
            status=response_object.get('Status'),
        )

    @staticmethod
    def SystemStatus(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return system_status.SystemStatus(
            engine_name=response_object.get('engineName'),
            services=SystemStatus.Services(response_object.get('services')),
            version=response_object.get('version'),
        )

    @staticmethod
    def Task(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        return system_status.Task(
            display_name=response_object.get('DisplayName'),
            name=response_object.get('Name'),
            start_time=from_date_string(response_object.get('StartTime')),
            stop_time=from_date_string(response_object.get('StopTime')),
            warning_count=response_object.get('WarningCount'),
        )

    @staticmethod
    def UpgradeInfo(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        return system_status.UpgradeInfo(
            id=response_object.get('Id'),
            start_time=from_date_string(response_object.get('StartTime')),
            versions=response_object.get('Versions'),
        )

    @staticmethod
    def UpgradeStatus(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        return system_status.UpgradeStatus(
            engine=SystemStatus.Engine(response_object.get('Engine')),
            status=response_object.get('Status'),
            upgrade_start_time=from_date_string(response_object.get('UpgradeStartTime')),
            upgrade_stop_time=from_date_string(response_object.get('UpgradeStopTime')),
            tasks_completed=[SystemStatus.Task(t) for t in response_object.get('TasksCompleted', [])],
            tasks_pending=[SystemStatus.Task(t) for t in response_object.get('TasksPending', [])],
            tasks_running=[SystemStatus.Task(t) for t in response_object.get('TasksRunning', [])],
        )

    @staticmethod
    def UpgradeSummary(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        return system_status.UpgradeSummary(
            status=response_object.get('Status'),
            upgrade_start_time=from_date_string(response_object.get('UpgradeStartTime')),
            upgrade_stop_time=from_date_string(response_object.get('UpgradeStopTime')),
            completed_tasks=response_object.get('CompletedTasks'),
            target_version=response_object.get('TargetVersion'),
            engines_complete=response_object.get('EnginesComplete'),
            engines_running=response_object.get('EnginesRunning'),
            engines_blocked=response_object.get('EnginesBlocked'),
            engines_in_error=response_object.get('EnginesInError'),
            engines_pending_install=response_object.get('EnginesPendingInstall'),
        )
