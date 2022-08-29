from typing import List
from pytpp.api.websdk.models import stats
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Stats(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Stats')
        self.GetCounters = self._GetCounters(api_obj=self._api_obj, url=f'{self._url}/GetCounters')
        self.Query = self._Query(api_obj=self._api_obj, url=f'{self._url}/Query')

    class _GetCounters(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                counters: List[stats.Counter] = ApiField(alias='Counters', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _Query(WebSdkEndpoint):
        def post(self, stats_type: str, tier: int, max_points: int, group_by_a: bool = None, group_by_b: bool = None,
                 group_by_c: bool = None, filter_a: str = None, filter_b: str = None, filter_c: str = None):
            body = {
                'StatsType': stats_type,
                'Tier'     : tier,
                'MaxPoints': max_points,
                'GroupByA' : group_by_a,
                'GroupByB' : group_by_b,
                'GroupByC' : group_by_c,
                'FilterA'  : filter_a,
                'FilterB'  : filter_b,
                'FilterC'  : filter_c
            }

            class Output(WebSdkOutputModel):
                results: List[stats.Result] = ApiField(alias='Results', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))
