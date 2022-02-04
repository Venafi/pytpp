from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.stats import Stats


class _Stats:
    def __init__(self, api_obj):
        self.GetCounters = self._GetCounters(api_obj=api_obj)
        self.Query = self._Query(api_obj=api_obj)
    
    class _GetCounters(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Stats/GetCounters')

        def post(self):
            
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def counters(self):
                    return [Stats.Counter(counter) for counter in self._from_json(key='Counters')]

                @property
                @api_response_property()
                def error(self) -> str:
                    return self._from_json(key='Error')

            return _Response(response=self._post(data={}))

    class _Query(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Stats/Query')

        def post(self, stats_type: str, tier: int, max_points: int, group_by_a: bool = None, group_by_b: bool = None,
                 group_by_c: bool = None, filter_a: str = None, filter_b: str = None, filter_c: str = None):
            body = {
                'StatsType': stats_type,
                'Tier': tier,
                'MaxPoints': max_points,
                'GroupByA': group_by_a,
                'GroupByB': group_by_b,
                'GroupByC': group_by_c,
                'FilterA': filter_a,
                'FilterB': filter_b,
                'FilterC': filter_c
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def results(self):
                    return [Stats.Result(result) for result in self._from_json(key='Results')]

            return _Response(response=self._post(data=body))
