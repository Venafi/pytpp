from __future__ import annotations
from pytpp.api.websdk.models.resultcodes import ResultCodes
from pytpp.api.api_base import ObjectModel, ApiField
from datetime import datetime
from typing import List, Literal

ClientType = Literal['VenafiAgent', 'AgentJuniorMachine', 'AgentJuniorUser', 'Portal', 'Agentless',
                     'PreEnrollment', 'iOS', 'Android']
OSNameType = Literal['AIX', 'Android', 'BlackBerry', 'BSD', 'HPux', 'iOS', 'Linux', 'MacOS', 'Other',
                     'Solaris', 'Unknown', 'Windows', 'zOS']
WorkType = Literal['Client Agent Configuration Work', 'Client Agent Automatic Upgrade Work',
                   'Client Agent Device Placement Work', 'Certificate Provisioning Work', 'Client Agent SSH Discovery Work',
                   'Client Agent SSH Provisioning Work', 'Client Agent SSH Key Usage Work', 'Client User Certificate Work',
                   'Client Certificate Work']


# region Models
class Result(ObjectModel):
    code: int = ApiField()

    @property
    def client_result(self) -> str:
        return ResultCodes.Client.get(self.code, 'Unknown')


class Work(ObjectModel):
    associated_groups: List[str] = ApiField(alias='AssociatedGroups', default_factory=list)
    work_dn: str = ApiField(alias='WorkDn')
    work_name: str = ApiField(alias='WorkName')
    work_type: WorkType = ApiField(alias='WorkType')


class Network(ObjectModel):
    ip_address: str = ApiField(alias='IpAddress')
    mac_address: str = ApiField(alias='MacAddress')


class Client(ObjectModel):
    client_id: int = ApiField(alias='ClientId')
    client_type: ClientType = ApiField(alias='ClientType')
    fqdn: str = ApiField(alias='Fqdn')
    os_name: OSNameType = ApiField(alias='OsName')
    username: str = ApiField(alias='Username')


class ClientDetails(ObjectModel):
    certificate_device: str = ApiField(alias='CertificateDevice')
    client_id: int = ApiField(alias='ClientId')
    client_type: ClientType = ApiField(alias='ClientType')
    client_version: str = ApiField(alias='ClientVersion')
    created_on: datetime = ApiField(alias='CreatedOn')
    dns_name: str = ApiField(alias='DnsName')
    effective_work: List[str] = ApiField(alias='EffectiveWork', default_factory=list)
    fqdn: str = ApiField(alias='Fqdn')
    groups: List[str] = ApiField(alias='Groups', default_factory=list)
    host_domain: str = ApiField(alias='HostDomain')
    hostname: str = ApiField(alias='Hostname')
    last_seen_on: datetime = ApiField(alias='LastSeenOn')
    networks: List[Network] = ApiField(alias='Networks', default_factory=list)
    os_build: str = ApiField(alias='OsBuild')
    os_name: OSNameType = ApiField(alias='OsName')
    os_service_pack: str = ApiField(alias='OsServicePack')
    os_version: str = ApiField(alias='OsVersion')
    region: str = ApiField(alias='Region')
    serial_number: str = ApiField(alias='SerialNumber')
    ssh_device: str = ApiField(alias='SshDevice')
    system_architecture: str = ApiField(alias='SystemArchitecture')
    system_chassis: str = ApiField(alias='SystemChassis')
    system_manufacturer: str = ApiField(alias='SystemManufacturer')
    system_model: str = ApiField(alias='SystemModel')
    trust_level: str = ApiField(alias='TrustLevel')
    username: str = ApiField(alias='Username')
    virtual_machine_id: str = ApiField(alias='VirtualMachineId')
