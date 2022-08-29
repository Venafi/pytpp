from typing import List, Union
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
from pytpp.api.websdk.models import identity as ident


class _Identity(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Identity')
        self.AddGroup = self._AddGroup(api_obj=self._api_obj, url=f'{self._url}/AddGroup')
        self.AddGroupMembers = self._AddGroupMembers(api_obj=self._api_obj, url=f'{self._url}/AddGroupMembers')
        self.Browse = self._Browse(api_obj=self._api_obj, url=f'{self._url}/Browse')
        self.GetAssociatedEntries = self._GetAssociatedEntries(api_obj=self._api_obj, url=f'{self._url}/GetAssociatedEntries')
        self.GetMembers = self._GetMembers(api_obj=self._api_obj, url=f'{self._url}/GetMembers')
        self.GetMemberships = self._GetMemberships(api_obj=self._api_obj, url=f'{self._url}/GetMemberships')
        self.Group = self._Group(api_obj=self._api_obj, url=f'{self._url}/Group')
        self.ReadAttribute = self._ReadAttribute(api_obj=self._api_obj, url=f'{self._url}/ReadAttribute')
        self.RemoveGroupMembers = self._RemoveGroupMembers(api_obj=self._api_obj, url=f'{self._url}/RemoveGroupMembers')
        self.RenameGroup = self._RenameGroup(api_obj=self._api_obj, url=f'{self._url}/RenameGroup')
        self.Self = self._Self(api_obj=self._api_obj, url=f'{self._url}/Self')
        self.SetPassword = self._SetPassword(api_obj=self._api_obj, url=f'{self._url}/SetPassword')
        self.Validate = self._Validate(api_obj=self._api_obj, url=f'{self._url}/Validate')

    class _AddGroup(WebSdkEndpoint):
        def post(self, name: str, members: List[Union[dict, ident.Identity]] = None, products: List[str] = None):
            body = {
                'Name'    : name,
                'Members' : members,
                'Products': products
            }

            class Output(WebSdkOutputModel):
                identity: ident.Identity = ApiField(alias='ID')
                invalid_members: List[ident.InvalidIdentity] = ApiField('InvalidMembers', default_factory=list)
                invalid_owners: List[ident.InvalidIdentity] = ApiField('InvalidOwners', default_factory=list)
                message: str = ApiField(alias='Message')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _AddGroupMembers(WebSdkEndpoint):
        def put(self, group: Union[dict, ident.Identity], members: List[Union[dict, ident.Identity]], show_members: bool = False):
            body = {
                'Group'      : group,
                'Members'    : members,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(alias='InvalidMembers', default_factory=list)
                members: List[ident.Identity] = ApiField(alias='Members', default_factory=list)
                message: str = ApiField(alias='Message')

            return generate_output(output_cls=Output, response=self._put(data=body))

    class _Browse(WebSdkEndpoint):
        # noinspection ALL
        def post(self, filter: str, limit: int, identity_type: int):
            body = {
                "Filter"      : filter,
                "Limit"       : limit,
                "IdentityType": identity_type
            }

            class Output(WebSdkOutputModel):
                identities: List[ident.Identity] = ApiField('Identities', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetAssociatedEntries(WebSdkEndpoint):
        def post(self, identity: Union[dict, ident.Identity]):
            body = {
                'ID': identity
            }

            class Output(WebSdkOutputModel):
                identities: List[ident.Identity] = ApiField('Identities', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetMembers(WebSdkEndpoint):
        def post(self, identity: Union[dict, ident.Identity], resolve_nested: bool = False):
            body = {
                'ID'           : identity,
                'ResolveNested': int(resolve_nested)
            }

            class Output(WebSdkOutputModel):
                identities: List[ident.Identity] = ApiField(alias='Identities', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetMemberships(WebSdkEndpoint):
        def post(self, identity: Union[dict, ident.Identity]):
            body = {
                'ID': identity
            }

            class Output(WebSdkOutputModel):
                identities: List[ident.Identity] = ApiField(alias='Identities', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Group(WebSdkEndpoint):
        def Prefix(self, prefix: str):
            return self._Prefix(api_obj=self._api_obj, url=f'{self._url}/{prefix}')

        class _Prefix(WebSdkEndpoint):
            def Principal(self, principal: str):
                return self._Principal(api_obj=self._api_obj, url=f'{self._url}/{principal}')

            class _Principal(WebSdkEndpoint):
                def delete(self):
                    class Output(WebSdkOutputModel):
                        message: str = ApiField(alias='Message')

                    return generate_output(output_cls=Output, response=self._delete())

    class _ReadAttribute(WebSdkEndpoint):
        def post(self, attribute_name: str, identity: Union[dict, ident.Identity]):
            body = {
                'ID'           : identity,
                'AttributeName': attribute_name
            }

            class Output(WebSdkOutputModel):
                attributes: List[str] = ApiField(alias='Attributes', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RemoveGroupMembers(WebSdkEndpoint):
        def put(self, group: Union[dict, ident.Identity], members: List[Union[dict, ident.Identity]], show_members: bool = False):
            body = {
                'Group'      : group,
                'Members'    : members,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(alias='InvalidMembers', default_factory=list)
                members: List[ident.Identity] = ApiField(alias='Members', default_factory=list)
                message: str = ApiField(alias='Message')

            return generate_output(output_cls=Output, response=self._put(data=body))

    class _RenameGroup(WebSdkEndpoint):
        def put(self, group: Union[dict, ident.Identity], new_group_name: str):
            body = {
                'Group'       : group,
                'NewGroupName': new_group_name
            }

            class Output(WebSdkOutputModel):
                identity: ident.Identity = ApiField(alias='ID')

            return generate_output(output_cls=Output, response=self._put(data=body))

    class _Self(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                identities: List[ident.Identity] = ApiField(alias='Identities', default_factory=list)

            return generate_output(output_cls=Output, response=self._get())

    class _SetPassword(WebSdkEndpoint):
        def post(self, identity: Union[dict, ident.Identity], password: str, old_password: str = None):
            body = {
                'ID'         : identity,
                'OldPassword': old_password,
                'Password'   : password
            }

            class Output(WebSdkOutputModel):
                identity: ident.Identity = ApiField(alias='ID')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Validate(WebSdkEndpoint):
        def post(self, identity: Union[dict, ident.Identity]):
            body = {
                'ID': identity
            }

            class Output(WebSdkOutputModel):
                identity: ident.Identity = ApiField(alias='ID')

            return generate_output(output_cls=Output, response=self._post(data=body))
