from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Result:
    code: int
    workflow_result: str


@dataclass
class Details:
    approval_explanation: str
    approval_from: str
    approvers: List[str]
    blocking: str
    created: datetime
    issued_due_to: str
    status: str
    updated: datetime
