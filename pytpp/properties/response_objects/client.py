from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.properties.response_objects.dataclasses import client


class Client:
    @staticmethod
    def Result(code: int):
        return client.Result(
            code=code,
            client_result=ResultCodes.Client.get(code, 'Unknown'),
        )

    @staticmethod
    def Client(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return client.Client(
            client_id=response_object.get('ClientId'),
            client_type=response_object.get('ClientType'),
            fqdn=response_object.get('FQDN'),
            os_name=response_object.get('OsName'),
            username=response_object.get('Username'),
        )

    @staticmethod
    def ClientDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return client.ClientDetails(
            certificate_device=response_object.get('CertificateDevice'),
            client_id=response_object.get('ClientId'),
            client_type=response_object.get('ClientType'),
            client_version=response_object.get('ClientVersion'),
            created_on=from_date_string(response_object.get('CreatedOn')),
            dns_name=response_object.get('DnsName'),
            effective_work=response_object.get('EffectiveWork'),
            fqdn=response_object.get('FQDN'),
            groups=response_object.get('Groups'),
            host_domain=response_object.get('HostDomain'),
            hostname=response_object.get('Hostname'),
            last_seen_on=from_date_string(response_object.get('LastSeenOn')),
            networks=[Client._Network(network) for network in response_object.get('Networks')],
            os_build=response_object.get('OsBuild'),
            os_name=response_object.get('OsName'),
            os_service_pack=response_object.get('OsServicePack'),
            os_version=response_object.get('OsVersion'),
            region=response_object.get('Region'),
            serial_number=response_object.get('SerialNumber'),
            ssh_device=response_object.get('SshDevice'),
            system_architecture=response_object.get('SystemArchitecture'),
            system_chassis=response_object.get('SystemChassis'),
            system_manufacturer=response_object.get('SystemManufacturer'),
            system_model=response_object.get('SystemModel'),
            trust_level=response_object.get('TrustLevel'),
            username=response_object.get('Username'),
            virtual_machine_id=response_object.get('VirtualMachineId'),
        )

    @staticmethod
    def Work(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return client.Work(
            associated_groups=response_object.get('AssociatedGroups'),
            work_dn=response_object.get('WorkDn'),
            work_name=response_object.get('WorkName'),
            work_type=response_object.get('WorkType'),
        )

    @staticmethod
    def _Network(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return client._Network(
            ip_address=response_object.get('IpAddress'),
            mac_address=response_object.get('MacAddress'),
        )
