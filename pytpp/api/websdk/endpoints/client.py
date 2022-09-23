from typing import List
from pytpp.api.websdk.models import client
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Client(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Client')
        self.Delete = self._Delete(api_obj=api_obj, url=f'{self._url}/Delete')
        self.Details = self._Details(api_obj=api_obj, url=f'{self._url}/Details')
        self.Work = self._Work(api_obj=api_obj, url=f'{self._url}/Work')

    def get(self, client_version: str = None, client_type: client.ClientType = None, host_name: str = None, ip_address: str = None,
            last_seen_on: str = None, last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
            os_name: client.OSNameType = None, os_version: str = None, region: str = None, serial_number: int = None, sid: str = None,
            user_name: str = None, virtual_machine_id: int = None):
        params = {
            'ClientVersion'    : client_version,
            'client.ClientType': client_type,
            'HostName'         : host_name,
            'IpAddress'        : ip_address,
            'LastSeenOn'       : last_seen_on,
            'LastSeenOnGreater': last_seen_on_greater,
            'LastSeenOnLess'   : last_seen_on_less,
            'MacAddress'       : mac_address,
            'OSName'           : os_name,
            'OSVersion'        : os_version,
            'Region'           : region,
            'SerialNumber'     : serial_number,
            'SID'              : sid,
            'UserName'         : user_name,
            'VirtualMachineId' : virtual_machine_id
        }

        class Output(WebSdkOutputModel):
            clients: List[client.Client] = ApiField(default_factory=list)
            error_description: str = ApiField(alias='error_description')
            error: str = ApiField(alias='error')

        return generate_output(response=self._get(params=params), output_cls=Output, root_field='clients')

    class _Delete(WebSdkEndpoint):
        def post(self, clients: List[client.Client], delete_associated_devices: bool = False):
            body = {
                'Clients'                : clients,
                'DeleteAssociatedDevices': delete_associated_devices
            }

            class Output(WebSdkOutputModel):
                deleted_count: int = ApiField(alias='DeletedCount')
                error_description: str = ApiField(alias='error_description')
                error: str = ApiField(alias='error')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Details(WebSdkEndpoint):
        def get(self, client_version: int = None, client_type: str = None, host_name: str = None, ip_address: str = None,
                last_seen_on: str = None, last_seen_on_greater: str = None, last_seen_on_less: str = None, mac_address: str = None,
                os_name: client.OSNameType = None, os_version: str = None, region: str = None, serial_number: int = None,
                sid: str = None, user_name: str = None, virtual_machine_id: int = None):
            params = {
                'ClientVersion'    : client_version,
                'ClientType'       : client_type,
                'HostName'         : host_name,
                'IpAddress'        : ip_address,
                'LastSeenOn'       : last_seen_on,
                'LastSeenOnGreater': last_seen_on_greater,
                'LastSeenOnLess'   : last_seen_on_less,
                'MacAddress'       : mac_address,
                'OSName'           : os_name,
                'OSVersion'        : os_version,
                'Region'           : region,
                'SerialNumber'     : serial_number,
                'SID'              : sid,
                'UserName'         : user_name,
                'VirtualMachineId' : virtual_machine_id
            }

            class Output(WebSdkOutputModel):
                details: List[client.ClientDetails] = ApiField(default_factory=list)
                error_description: str = ApiField(alias='error_description')
                error: str = ApiField(alias='error')

            return generate_output(response=self._get(params=params), output_cls=Output, root_field='details')

    class _Work(WebSdkEndpoint):
        def get(self, work_type: client.WorkType = None):
            params = {
                'client.WorkType': work_type
            }

            class Output(WebSdkOutputModel):
                works: List[client.Work] = ApiField(default_factory=list)
                error_description: str = ApiField(alias='error_description')
                error: str = ApiField(alias='error')

            return generate_output(response=self._get(params=params), output_cls=Output, root_field='works')
