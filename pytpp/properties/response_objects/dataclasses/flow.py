from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Result:
    code: int
    flow_result: str


@dataclass
class Ticket:
    approvals: 'List[Approval]'
    approvers: List[str]
    creation_time: datetime
    environment: 'List[KeyValue]'
    flow_process_id: int
    id: int
    identifier: str
    product_code: int
    remaining_uses: int
    required_approvals: int


@dataclass
class Approval:
    approval_time: datetime
    universal: str


@dataclass
class KeyValue:
    key: str
    value: str
