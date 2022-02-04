from pytpp.properties.response_objects.dataclasses import worfklow
from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string


class Workflow:
    @staticmethod
    def Result(code: int):
        return worfklow.Result(
            code=code,
            workflow_result=ResultCodes.Workflow.get(code, 'Unknown'),
        )

    @staticmethod
    def Details(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return worfklow.Details(
            approval_explanation=response_object.get('ApprovalExplanation'),
            approval_from=response_object.get('ApprovalFrom'),
            approvers=response_object.get('Approvers'),
            blocking=response_object.get('Blocking'),
            created=from_date_string(response_object.get('Created')),
            issued_due_to=response_object.get('IssuedDueTo'),
            status=response_object.get('Status'),
            updated=from_date_string(response_object.get('Updated')),
        )
