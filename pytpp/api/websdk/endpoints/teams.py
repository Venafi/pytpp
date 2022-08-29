from typing import List, Union
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
from pytpp.api.websdk.models import identity as ident


class _Teams(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Teams')
        self.AddTeamMembers = self._AddTeamMembers(api_obj=self._api_obj, url=f'{self._url}/AddTeamMembers')
        self.AddTeamOwners = self._AddTeamOwners(api_obj=self._api_obj, url=f'{self._url}/AddTeamOwners')
        self.DemoteTeamOwners = self._DemoteTeamOwners(api_obj=self._api_obj, url=f'{self._url}/DemoteTeamOwners')
        self.RemoveTeamMembers = self._RemoveTeamMembers(api_obj=self._api_obj, url=f'{self._url}/RemoveTeamMembers')
        self.RenameTeam = self._RenameTeam(api_obj=self._api_obj, url=f'{self._url}/RenameTeam')

    def post(self, name: str, owners: List[Union[dict, ident.Identity]], assets: List[str] = None, description: str = None,
             members: List[Union[dict, ident.Identity]] = None, products: List[str] = None):
        body = {
            'Assets'     : assets,
            'Description': description,
            'Name'       : name,
            'Owners'     : owners,
            'Members'    : members,
            'Products'   : products
        }

        class Output(WebSdkOutputModel):
            identity: ident.Identity = ApiField(default_factory=list, alias='ID')
            invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
            invalid_owners: List[ident.InvalidIdentity] = ApiField(alias='InvalidOwners', default_factory=list)
            message: str = ApiField(alias='Message')

        return generate_output(output_cls=Output, response=self._post(data=body))

    class _AddTeamMembers(WebSdkEndpoint):
        def put(self, members: List[Union[dict, ident.Identity]], team: Union[dict, ident.Identity] = None,
                show_members: bool = None):
            body = {
                'Members'    : members,
                'Team'       : team,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')

            return generate_output(output_cls=Output, response=self._put(data=body))

    class _AddTeamOwners(WebSdkEndpoint):
        def put(self, owners: List[Union[dict, ident.Identity]] = None, team: Union[dict, ident.Identity] = None, show_members: bool = None):
            body = {
                'Owners'     : owners,
                'Team'       : team,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')
                owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')

            return generate_output(output_cls=Output, response=self._put(data=body))

    class _DemoteTeamOwners(WebSdkEndpoint):
        def put(self, owners: List[Union[dict, ident.Identity]] = None, team: Union[dict, ident.Identity] = None,
                show_members: bool = None):
            body = {
                'Owners'     : owners,
                'Team'       : team,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')
                owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')

            return generate_output(output_cls=Output, response=self._put(data=body))

    def Prefix(self, prefix='local'):
        return self._Prefix(api_obj=self._api_obj, url=f'{self._url}/{prefix}')

    class _Prefix(WebSdkEndpoint):
        def Universal(self, universal):
            return self._Universal(api_obj=self._api_obj, url=f'{self._url}/{universal}')

        class _Universal(WebSdkEndpoint):
            def delete(self):
                class Output(WebSdkOutputModel):
                    message: str = ApiField(alias='Message')

                return generate_output(output_cls=Output, response=self._delete())

            def get(self):
                class Output(WebSdkOutputModel):
                    assets: List[str] = ApiField(default_factory=list, alias='Assets')
                    description: str = ApiField(alias='Description')
                    identity: ident.Identity = ApiField(alias='ID')
                    members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                    message: str = ApiField(alias='Message')
                    owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')
                    products: List[str] = ApiField(default_factory=list, alias='Products')

                return generate_output(output_cls=Output, response=self._get())

            def put(self, assets: List[str], description: str, name: str, owners: List[Union[dict, ident.Identity]],
                    members: List[Union[dict, ident.Identity]], products: List[str]):
                body = {
                    'Assets'     : assets,
                    'Description': description,
                    'Name'       : name,
                    'Owners'     : owners,
                    'Members'    : members,
                    'Products'   : products
                }

                class Output(WebSdkOutputModel):
                    identity: ident.Identity = ApiField(alias='ID')
                    invalid_owners: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidOwners')
                    invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                    message: str = ApiField(alias='Message')

                return generate_output(output_cls=Output, response=self._put(data=body))

    class _RemoveTeamMembers(WebSdkEndpoint):
        def put(self, team: Union[dict, ident.Identity], members: List[Union[dict, ident.Identity]] = None, show_members: bool = None):
            body = {
                'Team'       : team,
                'Members'    : members,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')
                owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')

            return generate_output(output_cls=Output, response=self._put(data=body))

    class _RenameTeam(WebSdkEndpoint):
        def put(self, team: Union[dict, ident.Identity], new_team_name: str):
            body = {
                'Team'       : team,
                'NewTeamName': new_team_name
            }

            class Output(WebSdkOutputModel):
                identity: ident.Identity = ApiField(alias='ID')
                message: str = ApiField(alias='Message')

            return generate_output(output_cls=Output, response=self._put(data=body))
