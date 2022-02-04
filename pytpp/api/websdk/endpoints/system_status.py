from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.system_status import SystemStatus
from pytpp.tools.helpers.date_converter import from_date_string

class _SystemStatus(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/SystemStatus')
        self.Upgrade = self._Upgrade(api_obj=api_obj)
        self.Version = self._Version(api_obj=api_obj)

    def get(self):
        class _Response(APIResponse):
            def __init__(self, response):
                super().__init__(response=response)

            @property
            @api_response_property()
            def engines(self):
                return [SystemStatus.SystemStatus(status) for status in self._from_json()]

        return _Response(response=self._get())

    class _Upgrade:
        def __init__(self, api_obj):
            self.Engine = self._Engine(api_obj=api_obj)
            self.Engines = self._Engines(api_obj=api_obj)
            self.History = self._History(api_obj=api_obj)
            self.Status = self._Status(api_obj=api_obj)
            self.Summary = self._Summary(api_obj=api_obj)

        class _Engine(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Engine')

            def get(self, guid: str, engine_id: str, upgrade_id: str = None):
                params = {
                    'guid': guid,
                    'Id': engine_id,
                    'UpgradeId': upgrade_id
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def engine(self):
                        return SystemStatus.Engine(self._from_json(key='Engine'))

                    @property
                    @api_response_property()
                    def status(self) -> str:
                        return self._from_json(key='Status')

                    @property
                    @api_response_property()
                    def upgrade_start_time(self):
                        return from_date_string(self._from_json(key='UpgradeStartTime'))

                    @property
                    @api_response_property()
                    def upgrade_stop_time(self):
                        return from_date_string(self._from_json(key='UpgradeStopTime'))

                    @property
                    @api_response_property()
                    def tasks_completed(self):
                        return [SystemStatus.Task(task) for task in self._from_json(key='TasksCompleted')]

                    @property
                    @api_response_property()
                    def tasks_pending(self):
                        return [SystemStatus.Task(task) for task in self._from_json(key='TasksPending')]

                    @property
                    @api_response_property()
                    def tasks_running(self):
                        return [SystemStatus.Task(task) for task in self._from_json(key='TasksRunning')]

                return _Response(response=self._get(params=params))

        class _Engines(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Engines')

            def get(self, upgrade_id: int = None):
                params = {
                    'UpgradeId': upgrade_id
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def engines(self):
                        return [SystemStatus.UpgradeStatus(engine) for engine in self._from_json(key='Engines')]

                return _Response(response=self._get(params=params))

        class _History(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/History')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def upgrade_history(self):
                        return [SystemStatus.UpgradeInfo(info) for info in self._from_json(key='UpgradeHistory')]

                return _Response(response=self._get())

        class _Status(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Status')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def upgrade_in_progress(self) -> bool:
                        return self._from_json(key='UpgradeInProgress')

                return _Response(response=self._get())

        class _Summary(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Summary')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def upgrade_summary(self):
                        return SystemStatus.UpgradeSummary(self._from_json(key='UpgradeSummary'))

                return _Response(response=self._get())

    class _Version(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SystemStatus/Version')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def version(self) -> str:
                    return self._from_json('Version')

            return _Response(response=self._get())
