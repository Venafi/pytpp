from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Result:
    code: int
    client_result: str


@dataclass
class Client:
    client_id: int
    client_type: str
    fqdn: str
    os_name: str
    username: str


@dataclass
class ClientDetails:
    certificate_device: str
    client_id: int
    client_type: str
    client_version: str
    created_on: datetime
    dns_name: str
    effective_work: list
    fqdn: str
    groups: list
    host_domain: str
    hostname: str
    last_seen_on: datetime
    networks: 'List[_Network]'
    os_build: str
    os_name: str
    os_service_pack: str
    os_version: str
    region: str
    serial_number: str
    ssh_device: str
    system_architecture: str
    system_chassis: str
    system_manufacturer: str
    system_model: str
    trust_level: str
    username: str
    virtual_machine_id: str


@dataclass
class Work:
    associated_groups: list
    work_dn: str
    work_name: str
    work_type: str


@dataclass
class _Network:
    ip_address: str
    mac_address: str
