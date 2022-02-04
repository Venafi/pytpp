from typing import List
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.identity import Identity


class _Teams(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Teams')
        self.AddTeamMembers = self._AddTeamMembers(api_obj=api_obj)
        self.AddTeamOwners = self._AddTeamOwners(api_obj=api_obj)
        self.DemoteTeamOwners = self._DemoteTeamOwners(api_obj=api_obj)
        self.RemoveTeamMembers = self._RemoveTeamMembers(api_obj=api_obj)
        self.RenameTeam = self._RenameTeam(api_obj=api_obj)

    def post(self, name: str, owners: list, assets: list = None, description: str = None, members: list = None,
             products: list = None):
        body = {
            'Assets': assets,
            'Description': description,
            'Name': name,
            'Owners': owners,
            'Members': members,
            'Products': products
        }

        class _Response(APIResponse):
            def __init__(self, response):
                super().__init__(response=response)

            @property
            @api_response_property()
            def identity(self):
                return [Identity.Identity(owner) for owner in self._from_json(key='Owners')]

            @property
            @api_response_property()
            def invalid_members(self):
                return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

        return _Response(response=self._post(data=body))

    class _AddTeamMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/AddTeamMembers')

        def put(self, members: list, team: dict = None, show_members: bool = None):
            body = {
                'Members': members,
                'Team': team,
                'ShowMembers': show_members
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def invalid_members(self):
                    return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

                @property
                @api_response_property()
                def members(self):
                    return [Identity.Identity(member) for member in self._from_json(key='Members')]

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json(key='Message')

            return _Response(response=self._put(data=body))

    class _AddTeamOwners(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/AddTeamOwners')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def owners(self):
                    return [Identity.Identity(owner) for owner in self._from_json(key='Owners')]

                @property
                @api_response_property()
                def members(self):
                    return [Identity.Identity(member) for member in self._from_json(key='Members')]

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json(key='Message')

            return _Response(response=self._put(data=body))

    class _DemoteTeamOwners(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/DemoteTeamOwners')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def invalid_owners(self):
                    return [Identity.InvalidIdentity(owner) for owner in self._from_json(key='InvalidOwners')]

                @property
                @api_response_property()
                def owners(self):
                    return [Identity.Identity(owner) for owner in self._from_json(key='Owners')]

                @property
                @api_response_property()
                def members(self):
                    return [Identity.Identity(member) for member in self._from_json(key='Members')]

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json(key='Message')

            return _Response(response=self._put(data=body))

    def Prefix(self, prefix='local'):
        return self._Prefix(prefix=prefix, api_obj=self._api_obj)

    class _Prefix:
        def __init__(self, prefix: str, api_obj):
            self._prefix = prefix
            self._api_obj = api_obj

        def Universal(self, universal):
            return self._Universal(
                prefix=self._prefix,
                universal=universal,
                api_obj=self._api_obj
            )

        class _Universal(API):
            def __init__(self, prefix: str, universal: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/Teams/{prefix}/{universal}')

            def delete(self):
                
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                return _Response(response=self._delete())

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def assets(self) -> List[str]:
                        return self._from_json(key='Assets')

                    @property
                    @api_response_property()
                    def description(self) -> str:
                        return self._from_json(key='Description')

                    @property
                    @api_response_property()
                    def identity(self):
                        return Identity.Identity(self._from_json(key='ID'))

                    @property
                    @api_response_property()
                    def members(self):
                        return [Identity.Identity(member) for member in self._from_json(key='Members')]

                    @property
                    @api_response_property()
                    def owners(self):
                        return [Identity.Identity(owner) for owner in self._from_json(key='Owners')]

                    @property
                    @api_response_property()
                    def products(self) -> List[str]:
                        return self._from_json(key='Products')

                return _Response(response=self._get())

            def put(self, assets: list, description: str, name: str, owners: list, members: list, products: list):
                body = {
                    'Assets': assets,
                    'Description': description,
                    'Name': name,
                    'Owners': owners,
                    'Members': members,
                    'Products': products
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def identity(self):
                        return Identity.Identity(self._from_json(key='ID'))

                    @property
                    @api_response_property()
                    def invalid_owners(self):
                        return [Identity.InvalidIdentity(owner) for owner in self._from_json(key='InvalidOwners')]

                    @property
                    @api_response_property()
                    def invalid_members(self):
                        return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                return _Response(response=self._put(data=body))

    class _RemoveTeamMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/RemoveTeamMembers')

        def put(self, team: dict, members: list = None, show_members: bool = None):
            body = {
                'Team': team,
                'Members': members,
                'ShowMembers': show_members
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def invalid_members(self):
                    return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

                @property
                @api_response_property()
                def members(self):
                    return [Identity.Identity(member) for member in self._from_json(key='Members')]

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json(key='Message')

                @property
                @api_response_property()
                def owners(self):
                    return [Identity.Identity(owner) for owner in self._from_json(key='Owners')]

            return _Response(response=self._put(data=body))

    class _RenameTeam(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Teams/RenameTeam')

        def put(self, team: str, new_team_name: str):
            body = {
                'Team'       : team,
                'NewTeamName': new_team_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identity(self):
                    return Identity.Identity(self._from_json(key='ID'))

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json(key='Message')

            return _Response(response=self._put(data=body))
