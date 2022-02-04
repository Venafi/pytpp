from typing import List
from dataclasses import dataclass


@dataclass
class Response:
    success: bool
    error_code: int
    error_message: str


@dataclass
class ProcessingDetails:
    status: str
    status_description: str


@dataclass
class CertificateDetails:
    ca_fingerprint_sha256: str
    certificate_fingerprint_sha256: str
    certificate_type: str
    extensions: dict
    key_id: str
    key_type: str
    principals: List[str]
    public_key_fingerprint_sha256: str
    serial_number: str
    valid_from: int
    valid_to: int


@dataclass
class RequestDetails:
    originating_ip: str
    requested_by: str


@dataclass
class APIClient:
    allowed_to_request_certificate_identifier: bool
    allowed_to_request_extensions: bool
    allowed_to_request_force_command: bool
    allowed_to_request_principals: bool
    allowed_to_request_source_addresses: bool


@dataclass
class Certificate:
    allowed_private_key_algorithms: List[str]
    allowed_private_key_reuse: bool
    certificate_destination_dn: str
    default_private_key_algorithm: str
    signature_hashing_algorithm: str
    type: str
    validity_period: str


@dataclass
class CAKeyPair:
    created_on: str
    dn: str
    fingerprint_sha256: str
    guid: str
    key_algorithm: str
    name: str
    public_key_data: str
