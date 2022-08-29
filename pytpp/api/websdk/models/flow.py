from __future__ import annotations
from pytpp.api.websdk.models.resultcodes import ResultCodes
from pytpp.api.api_base import ObjectModel, ApiField
from datetime import datetime
from typing import List


class Result(ObjectModel):
    code: int = ApiField()

    @property
    def flow_result(self) -> str:
        return ResultCodes.Flow.get(self.code, 'Unknown')


class Approval(ObjectModel):
    approval_time: datetime = ApiField(alias='ApprovalTime')
    universal: str = ApiField(alias='Universal')


class KeyValue(ObjectModel):
    key: str = ApiField(alias='Key')
    value: str = ApiField(alias='Value')


class Ticket(ObjectModel):
    approvals: List[Approval] = ApiField(alias='Approvals', default_factory=list)
    approvers: List[str] = ApiField(alias='Approvers', default_factory=list)
    creation_time: datetime = ApiField(alias='CreationTime')
    environment: List[KeyValue] = ApiField(alias='Environment', default_factory=list)
    flow_process_id: int = ApiField(alias='FlowProcessId')
    id: int = ApiField(alias='Id')
    identifier: str = ApiField(alias='Identifier')
    product_code: int = ApiField(alias='ProductCode')
    remaining_uses: int = ApiField(alias='RemainingUses')
    required_approvals: int = ApiField(alias='RequiredApprovals')
