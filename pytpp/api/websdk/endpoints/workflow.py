from datetime import datetime
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
from pytpp.api.websdk.models import workflow, identity as ident
from typing import List


class _Workflow(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Workflow')
        self.Ticket = self._Ticket(api_obj=api_obj, url=f'{self._url}/Ticket')

    class _Ticket(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Create = self._Create(api_obj=self._api_obj, url=f'{self._url}/Create')
            self.Delete = self._Delete(api_obj=self._api_obj, url=f'{self._url}/Delete')
            self.Details = self._Details(api_obj=self._api_obj, url=f'{self._url}/Details')
            self.Enumerate = self._Enumerate(api_obj=self._api_obj, url=f'{self._url}/Enumerate')
            self.Exists = self._Exists(api_obj=self._api_obj, url=f'{self._url}/Exists')
            self.Status = self._Status(api_obj=self._api_obj, url=f'{self._url}/Status')
            self.UpdateStatus = self._UpdateStatus(api_obj=self._api_obj, url=f'{self._url}/UpdateStatus')

        class _Create(WebSdkEndpoint):
            def post(self, object_dn: str, approvers: List[ident.Identity], reason: str, workflow_dn: str, user_data: str = None):
                body = {
                    'ObjectDN'  : object_dn,
                    'Approvers' : approvers,
                    'Reason'    : reason,
                    'UserData'  : user_data,
                    'WorkflowDN': workflow_dn
                }

                class Output(WebSdkOutputModel):
                    guid: str = ApiField(alias='GUID')
                    result: workflow.Result = ApiField(alias='Result')

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Delete(WebSdkEndpoint):
            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Output(WebSdkOutputModel):
                    result: workflow.Result = ApiField(alias='Result')

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Details(WebSdkEndpoint):
            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Output(WebSdkOutputModel):
                    approval_explanation: str = ApiField(alias='ApprovalExplanation')
                    approval_from: str = ApiField(alias='ApprovalFrom')
                    approval_reason: str = ApiField(alias='ApprovalReason')
                    approvers: List[str] = ApiField(alias='Approvers', default_factory=list)
                    blocking: str = ApiField(alias='Blocking')
                    created: datetime = ApiField(alias='Created')
                    issued_due_to: str = ApiField(alias='IssuedDueTo')
                    result: workflow.Result = ApiField(alias='Result')
                    status: str = ApiField(alias='Status')
                    updated: datetime = ApiField(alias='Updated')

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Enumerate(WebSdkEndpoint):
            def post(self, object_dn: str = None, user_data: str = None):
                body = {
                    'ObjectDN': object_dn,
                    'UserData': user_data
                }

                class Output(WebSdkOutputModel):
                    guids: List[str] = ApiField(default_factory=list, alias='GUIDS')
                    result: workflow.Result = ApiField(alias='Result')

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Exists(WebSdkEndpoint):
            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Output(WebSdkOutputModel):
                    result: workflow.Result = ApiField(alias='Result')

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Status(WebSdkEndpoint):
            def post(self, guid: str):
                body = {
                    'GUID': guid
                }

                class Output(WebSdkOutputModel):
                    status: str = ApiField(alias='Status')
                    result: workflow.Result = ApiField(alias='Result')

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _UpdateStatus(WebSdkEndpoint):
            def post(self, guid: str, status: str, explanation: str = None, scheduled_start: str = None,
                     scheduled_stop: str = None, approvers: List[str] = None, object_dn: str = None,
                     reason: str = None, user_data=None):
                body = {
                    'GUID'          : guid,
                    'Status'        : status,
                    'Explanation'   : explanation,
                    'ScheduledStart': scheduled_start,
                    'ScheduledStop' : scheduled_stop,
                    'Approvers'     : approvers,
                    'ObjectDN'      : object_dn,
                    'Reason'        : reason,
                    'UserData'      : user_data
                }

                class Output(WebSdkOutputModel):
                    result: workflow.Result = ApiField(alias='Result')

                return generate_output(output_cls=Output, response=self._post(data=body))
