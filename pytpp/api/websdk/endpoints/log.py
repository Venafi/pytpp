from typing import List
from pytpp.api.websdk.models import log
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Log(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Log')
        self.LogSchema = self._LogSchema(api_obj=api_obj, url=f'{self._url}/LogSchema')

    def get(self, component: str = None, from_time: str = None, grouping: int = None, id: int = None,
            limit: int = None, offset: int = None, order: str = None, severity: str = None, text1: str = None,
            text2: str = None, to_time: str = None, value1: str = None, value2: str = None):
        params = {
            'Component': component,
            'FromTime' : from_time,
            'Grouping' : grouping,
            'Id'       : id,
            'Limit'    : limit,
            'Offset'   : offset,
            'Order'    : order,
            'Severity' : severity,
            'Text1'    : text1,
            'Text2'    : text2,
            'ToTime'   : to_time,
            'Value1'   : value1,
            'Value2'   : value2
        }

        class Output(WebSdkOutputModel):
            log_events: List[log.LogEvent] = ApiField(default_factory=list, alias='LogEvents')

        return generate_output(output_cls=Output, response=self._get(params=params))

    def post(self, component: str, id: int, grouping: int = None, severity: int = None, source_ip: str = None,
             text1: str = None, text2: str = None, value1: str = None, value2: str = None):
        body = {
            'Component': component,
            'ID'       : id,
            'Grouping' : grouping,
            'Severity' : severity,
            'SourceIp' : source_ip,
            'Text1'    : text1,
            'Text2'    : text2,
            'Value1'   : value1,
            'Value2'   : value2
        }

        class Output(WebSdkOutputModel):
            log_result: int = ApiField(alias='LogResult')

        return generate_output(output_cls=Output, response=self._post(data=body))

    def Guid(self, guid: str):
        return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

    class _Guid(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                log_events: List[log.LogEvent] = ApiField(default_factory=list, alias='LogEvents')

            return generate_output(output_cls=Output, response=self._get())

    class _LogSchema(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                log_event_application_definitions: List[log.LogEventApplicationDefinition] = ApiField(
                    alias='LogEventApplicationDefinitions'
                )
                log_event_definitions: List[log.LogEventDefinition] = ApiField(alias='LogEventDefinitions', default_factory=list)
                log_result: int = ApiField(alias='LogResult')

            return generate_output(output_cls=Output, response=self._get())
