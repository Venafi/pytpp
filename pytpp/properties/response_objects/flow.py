from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.properties.response_objects.dataclasses import flow


class Flow:
    @staticmethod
    def Result(code: int):
        return flow.Result(
            code=code,
            flow_result=ResultCodes.Flow.get(code, 'Unknown'),
        )

    @staticmethod
    def Ticket(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return flow.Ticket(
            approvals=[Flow.Approval(a) for a in response_object.get('Approvals')],
            approvers=response_object.get('Approvers'),
            creation_time=from_date_string(response_object.get('CreationTime')),
            environment=[Flow.KeyValue(i) for i in response_object.get('Environment')],
            flow_process_id=response_object.get('FlowProcessId'),
            id=response_object.get('Id'),
            identifier=response_object.get('Identifier'),
            product_code=response_object.get('ProductCode'),
            remaining_uses=response_object.get('RemainingUses'),
            required_approvals=response_object.get('RequiredApprovals'),
        )

    @staticmethod
    def Approval(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return flow.Approval(
            approval_time=from_date_string(response_object.get('ApprovalTime')),
            universal=response_object.get('Universal'),
        )

    @staticmethod
    def KeyValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return flow.KeyValue(
            key=response_object.get('Key'),
            value=response_object.get('Value'),
        )
