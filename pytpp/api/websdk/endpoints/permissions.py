from typing import List 
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.permissions import Permissions


class _Permissions:
    def __init__(self, api_obj):
        self.Object = self._Object(api_obj=api_obj)
        self.Refresh = self._Refresh(api_obj=api_obj)

    class _Object:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid(API):
            def __init__(self, guid: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/Permissions/Object/{guid}')
                self._guid = guid

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def principals(self) -> List[str]:
                        return self._from_json()

                return _Response(response=self._get())

            def Ptype(self, ptype='Local'):
                return self._Ptype(guid=self._guid, ptype=ptype, api_obj=self._api_obj)

            class _Ptype:
                def __init__(self, guid:str, ptype: str, api_obj):
                    self._guid = guid
                    self._ptype = ptype
                    self._api_obj = api_obj

                def Pname(self, pname):
                    return self._Pname(guid=self._guid, ptype=self._ptype, pname=pname, api_obj=self._api_obj)

                def Principal(self, uuid: str):
                    return self._Principal(guid=self._guid, ptype=self._ptype, uuid=uuid, api_obj=self._api_obj)

                class _Pname:
                    def __init__(self, guid: str, ptype: str, pname: str, api_obj):
                        self._guid = guid
                        self._ptype = ptype
                        self._pname = pname
                        self._api_obj = api_obj

                    def Principal(self, principal: str):
                        return self._Principal(guid=self._guid, ptype=self._ptype, pname=self._pname,
                                              principal=principal, api_obj=self._api_obj)

                    class _Principal(API):
                        def __init__(self, guid: str, ptype: str, pname: str, principal: str, api_obj):
                            super().__init__(
                                api_obj=api_obj,
                                url=f'/Permissions/Object/{guid}/{ptype}/{pname}/{principal}'
                            )
                            self.Effective = self._Effective(guid=guid, ptype=ptype, pname=pname, principal=principal, api_obj=api_obj)

                        def delete(self):
                            return APIResponse(response=self._delete())

                        def get(self):
                            class _Response(APIResponse):
                                def __init__(self, response):
                                    super().__init__(response=response)

                                @property
                                @api_response_property()
                                def explicit_permissions(self):
                                    return Permissions.Permissions(self._from_json(key='ExplicitPermissions'))

                                @property
                                @api_response_property()
                                def implicit_permissions(self):
                                    return Permissions.Permissions(self._from_json(key='ImplicitPermissions'))

                            return _Response(response=self._get())

                        def post(self, is_associate_allowed: bool = None, is_create_allowed: bool = None, is_delete_allowed: bool = None,
                                 is_manage_permissions_allowed: bool = None, is_policy_write_allowed: bool = None,
                                 is_private_key_read_allowed: bool = None, is_private_key_write_allowed: bool = None, is_read_allowed: bool = None,
                                 is_rename_allowed: bool = None, is_revoke_allowed: bool = None, is_view_allowed: bool = None,
                                 is_write_allowed: bool = None):
                            body = {
                                'IsAssociateAllowed': is_associate_allowed,
                                'IsCreateAllowed': is_create_allowed,
                                'IsDeleteAllowed': is_delete_allowed,
                                'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                                'IsPolicyWriteAllowed': is_policy_write_allowed,
                                'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                                'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                                'IsReadAllowed': is_read_allowed,
                                'IsRenameAllowed': is_rename_allowed,
                                'IsRevokeAllowed': is_revoke_allowed,
                                'IsViewAllowed': is_view_allowed,
                                'IsWriteAllowed': is_write_allowed
                            }

                            return APIResponse(response=self._post(data=body))

                        def put(self, is_associate_allowed: bool = None, is_create_allowed: bool = None, is_delete_allowed: bool = None,
                                is_manage_permissions_allowed: bool = None, is_policy_write_allowed: bool = None,
                                is_private_key_read_allowed: bool = None, is_private_key_write_allowed: bool = None, is_read_allowed: bool = None,
                                is_rename_allowed: bool = None, is_revoke_allowed: bool = None, is_view_allowed: bool = None,
                                is_write_allowed: bool = None):
                            body = {
                                'IsAssociateAllowed': is_associate_allowed,
                                'IsCreateAllowed': is_create_allowed,
                                'IsDeleteAllowed': is_delete_allowed,
                                'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                                'IsPolicyWriteAllowed': is_policy_write_allowed,
                                'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                                'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                                'IsReadAllowed': is_read_allowed,
                                'IsRenameAllowed': is_rename_allowed,
                                'IsRevokeAllowed': is_revoke_allowed,
                                'IsViewAllowed': is_view_allowed,
                                'IsWriteAllowed': is_write_allowed
                            }

                            return APIResponse(response=self._put(data=body))

                        class _Effective(API):
                            def __init__(self, guid: str, ptype: str, pname: str, principal: str, api_obj):
                                super().__init__(
                                    api_obj=api_obj,
                                    url=f'/Permissions/Object/{guid}/{ptype}/{pname}/{principal}/Effective'
                                )

                            def get(self):
                                class _Response(APIResponse):
                                    def __init__(self, response):
                                        super().__init__(response=response)

                                    @property
                                    @api_response_property()
                                    def effective_permissions(self):
                                        return Permissions.Permissions(self._from_json('EffectivePermissions'))

                                return _Response(response=self._get())

                class _Principal(API):
                    def __init__(self, guid: str, ptype: str, uuid: str, api_obj):
                        super().__init__(
                            api_obj=api_obj,
                            url=f'/Permissions/Object/{guid}/{ptype}/{uuid}'
                        )
                        self.Effective = self._Effective(guid=guid, uuid=uuid, api_obj=api_obj)

                    def delete(self):
                        return APIResponse(response=self._delete())

                    def get(self):
                        class _Response(APIResponse):
                            def __init__(self, response):
                                super().__init__(response=response)

                            @property
                            @api_response_property()
                            def explicit_permissions(self):
                                return Permissions.Permissions(self._from_json('ExplicitPermissions'))

                            @property
                            @api_response_property()
                            def implicit_permissions(self):
                                return Permissions.Permissions(self._from_json('ImplicitPermissions'))

                        return _Response(response=self._get())

                    def post(self, is_associate_allowed: bool = None, is_create_allowed: bool = None, is_delete_allowed: bool = None,
                             is_manage_permissions_allowed: bool = None, is_policy_write_allowed: bool = None,
                             is_private_key_read_allowed: bool = None, is_private_key_write_allowed: bool = None, is_read_allowed: bool = None,
                             is_rename_allowed: bool = None, is_revoke_allowed: bool = None, is_view_allowed: bool = None,
                             is_write_allowed: bool = None):
                        body = {
                           'IsAssociateAllowed': is_associate_allowed,
                           'IsCreateAllowed': is_create_allowed,
                           'IsDeleteAllowed': is_delete_allowed,
                           'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                           'IsPolicyWriteAllowed': is_policy_write_allowed,
                           'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                           'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                           'IsReadAllowed': is_read_allowed,
                           'IsRenameAllowed': is_rename_allowed,
                           'IsRevokeAllowed': is_revoke_allowed,
                           'IsViewAllowed': is_view_allowed,
                           'IsWriteAllowed': is_write_allowed
                        }

                        return APIResponse(response=self._post(data=body))

                    def put(self, is_associate_allowed: bool = None, is_create_allowed: bool = None, is_delete_allowed: bool = None,
                            is_manage_permissions_allowed: bool = None, is_policy_write_allowed: bool = None,
                            is_private_key_read_allowed: bool = None, is_private_key_write_allowed: bool = None, is_read_allowed: bool = None,
                            is_rename_allowed: bool = None, is_revoke_allowed: bool = None, is_view_allowed: bool = None,
                            is_write_allowed: bool = None):
                        body = {
                            'IsAssociateAllowed': is_associate_allowed,
                            'IsCreateAllowed': is_create_allowed,
                            'IsDeleteAllowed': is_delete_allowed,
                            'IsManagePermissionsAllowed': is_manage_permissions_allowed,
                            'IsPolicyWriteAllowed': is_policy_write_allowed,
                            'IsPrivateKeyReadAllowed': is_private_key_read_allowed,
                            'IsPrivateKeyWriteAllowed': is_private_key_write_allowed,
                            'IsReadAllowed': is_read_allowed,
                            'IsRenameAllowed': is_rename_allowed,
                            'IsRevokeAllowed': is_revoke_allowed,
                            'IsViewAllowed': is_view_allowed,
                            'IsWriteAllowed': is_write_allowed
                        }

                        return APIResponse(response=self._put(data=body))

                    class _Effective(API):
                        def __init__(self, guid: str, uuid: str, api_obj):
                            super().__init__(
                                api_obj=api_obj,
                                url=f'/Permissions/Object/{guid}/Local/{uuid}/Effective'
                            )

                        def get(self):
                            class _Response(APIResponse):
                                def __init__(self, response):
                                    super().__init__(response=response)

                                @property
                                @api_response_property()
                                def effective_permissions(self):
                                    return Permissions.Permissions(self._from_json('EffectivePermissions'))

                            return _Response(response=self._get())

    class _Refresh(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Permissions/Refresh')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self) -> int:
                    return self._from_json('Result')

            return _Response(response=self._get())
