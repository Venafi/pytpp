from typing import List 
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.identity import Identity


class _Identity:
    def __init__(self, api_obj):
        self.AddGroup = self._AddGroup(api_obj=api_obj)
        self.AddGroupMembers = self._AddGroupMembers(api_obj=api_obj)
        self.Browse = self._Browse(api_obj=api_obj)
        self.GetAssociatedEntries = self._GetAssociatedEntries(api_obj=api_obj)
        self.GetMembers = self._GetMembers(api_obj=api_obj)
        self.GetMemberships = self._GetMemberships(api_obj=api_obj)
        self.Group = self._Group(api_obj=api_obj)
        self.ReadAttribute = self._ReadAttribute(api_obj=api_obj)
        self.RemoveGroupMembers = self._RemoveGroupMembers(api_obj=api_obj)
        self.RenameGroup = self._RenameGroup(api_obj=api_obj)
        self.Self = self._Self(api_obj=api_obj)
        self.SetPassword = self._SetPassword(api_obj=api_obj)
        self.Validate = self._Validate(api_obj=api_obj)

    class _AddGroup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/AddGroup')

        def post(self, name: str, members: list = None):
            body = {
                'Name': name,
                'Members': members
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identity(self):
                    return Identity.Identity(self._from_json('ID'))

                @property
                @api_response_property()
                def invalid_members(self):
                    return [Identity.InvalidIdentity(im) for im in self._from_json(key='InvalidMembers', return_on_error=list)]

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json(key='Message', return_on_error=str)

            return _Response(response=self._post(data=body))

    class _AddGroupMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/AddGroupMembers')

        def put(self, group: dict, members: list, show_members: bool = False):
            body = {
                'Group': group,
                'Members': members,
                'ShowMembers': show_members
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def invalid_members(self):
                    return [Identity.InvalidIdentity(im) for im in self._from_json('InvalidMembers', return_on_error=list)]

                @property
                @api_response_property()
                def members(self):
                    return [Identity.Identity(m) for m in self._from_json('Members', return_on_error=list)]

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json('Message')

            return _Response(response=self._put(data=body))

    class _Browse(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/Browse')

        def post(self, filter: str, limit: int, identity_type: int):
            body = {
                "Filter": filter,
                "Limit": limit,
                "IdentityType": identity_type
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identities(self):
                    return [Identity.Identity(i) for i in self._from_json(key='Identities', return_on_error=list)]

            return _Response(response=self._post(data=body))

    class _GetAssociatedEntries(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/GetAssociatedEntries')

        def post(self, identity: dict):
            body = {
                'ID': identity
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identities(self):
                    return [Identity.Identity(i) for i in self._from_json(key='Identities', return_on_error=list)]

            return _Response(response=self._post(data=body))

    class _GetMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/GetMembers')

        def post(self, identity: dict, resolve_nested: bool = False):
            body = {
                'ID': identity,
                'ResolveNested': int(resolve_nested)
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identities(self):
                    return [Identity.Identity(i) for i in self._from_json(key='Identities', return_on_error=list)]

            return _Response(response=self._post(data=body))

    class _GetMemberships(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/GetMemberships')

        def post(self, identity: dict):
            body = {
                'ID': identity
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identities(self):
                    return [Identity.Identity(i) for i in self._from_json(key='Identities', return_on_error=list)]

            return _Response(response=self._post(data=body))

    class _Group:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Prefix(self, prefix: str):
            return self._Prefix(prefix=prefix, api_obj=self._api_obj)

        class _Prefix:
            def __init__(self, prefix: str, api_obj):
                self._prefix = prefix
                self._api_obj = api_obj

            def Principal(self, principal: str):
                return self._Principal(prefix=self._prefix, principal=principal, api_obj=self._api_obj)

            class _Principal(API):
                def __init__(self, prefix: str, principal: str, api_obj):
                    super().__init__(api_obj=api_obj, url=f'/Identity/Group/{prefix}/{principal}')

                def delete(self):
                    class _Response(APIResponse):
                        def __init__(self, response):
                            super().__init__(response=response)

                        @property
                        @api_response_property()
                        def message(self) -> str:
                            return self._from_json('Message')

                    return _Response(response=self._delete())

    class _ReadAttribute(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/ReadAttribute')

        def post(self, attribute_name: str, identity: dict):
            body = {
                'ID': identity,
                'AttributeName': attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def attributes(self) -> List[str]:
                    return self._from_json(key='Attributes')

            return _Response(response=self._post(data=body))

    class _RemoveGroupMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/RemoveGroupMembers')

        def put(self, group: dict, members: list, show_members: bool = False):
            body = {
                'Group': group,
                'Members': members,
                'ShowMembers': show_members
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def invalid_members(self):
                    return [Identity.InvalidIdentity(im) for im in self._from_json('InvalidMembers', return_on_error=list)]

                @property
                @api_response_property()
                def members(self):
                    return [Identity.Identity(m) for m in self._from_json('Members', return_on_error=list)]

                @property
                @api_response_property()
                def message(self) -> str:
                    return self._from_json('Message')

            return _Response(response=self._put(data=body))

    class _RenameGroup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/RenameGroup')

        def put(self, group: dict, new_group_name: str):
            body = {
                'Group': group,
                'NewGroupName': new_group_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identity(self):
                    return Identity.Identity(self._from_json('ID'))

            return _Response(response=self._put(data=body))

    class _Self(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/Self')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identities(self):
                    return [Identity.Identity(i) for i in self._from_json(key='Identities')]

            return _Response(response=self._get())

    class _SetPassword(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/SetPassword')

        def post(self, identity: dict, password: str, old_password: str = None):
            body = {
                'ID': identity,
                'OldPassword': old_password,
                'Password': password
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identity(self):
                    return Identity.Identity(self._from_json('ID'))

            return _Response(response=self._post(data=body))

    class _Validate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Identity/Validate')

        def post(self, identity: dict):
            body = {
                'ID': identity
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def identity(self):
                    return Identity.Identity(self._from_json('ID'))

            return _Response(response=self._post(data=body))
