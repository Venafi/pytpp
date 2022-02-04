from typing import List
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Response:
    success: bool
    error_code: int
    error_message: str


@dataclass
class ConnectionResult:
    device_guid: str
    error: str
    success: bool


@dataclass
class DeviceData:
    dn: str
    device_guid: str
    host_name: str
    is_compliant: bool
    type: str


@dataclass
class KeyData:
    active_from: datetime
    algorithm: str
    allowed_source_restriction: List[str]
    approver: List[str]
    comment: str
    denied_source_restriction: List[str]
    device_guid: str
    filepath: str
    forced_command: str
    format: str
    is_encrypted: bool
    key_id: int
    keysetid: str
    last_used: datetime
    length: int
    notes: str
    options: List[str]
    process_error: str
    process_status: str
    reason: str
    rotation_stage: int
    type: str
    username: str
    violation_status: List[int]


@dataclass
class KeySetData:
    access: str
    algorithm: str
    fingerprint_md5: str
    fingerprint_sha256: str
    keysetid: str
    last_rotation_date: datetime
    last_used: datetime
    length: int
    private_keys: 'List[KeyData]'
    process_error: str
    process_status: str
    public_keys: 'List[KeyData]'
    rotation_stage: int
    type: str
    violation_status: list


@dataclass
class KeyUsageData:
    alert: int
    authorized_key_id: int
    client_name: str
    fingerprint: str
    key_usage_id: int
    keyset_id: str
    last_used: datetime
    private_key_id: int
    server_account: str
    server_name: str
