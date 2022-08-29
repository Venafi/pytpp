from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField


class Permissions(ObjectModel):
    is_associate_allowed: bool = ApiField(alias='IsAssociateAllowed')
    is_create_allowed: bool = ApiField(alias='IsCreateAllowed')
    is_delete_allowed: bool = ApiField(alias='IsDeleteAllowed')
    is_manage_permissions_allowed: bool = ApiField(alias='IsManagePermissionsAllowed')
    is_policy_write_allowed: bool = ApiField(alias='IsPolicyWriteAllowed')
    is_private_key_read_allowed: bool = ApiField(alias='IsPrivateKeyReadAllowed')
    is_private_key_write_allowed: bool = ApiField(alias='IsPrivateKeyWriteAllowed')
    is_read_allowed: bool = ApiField(alias='IsReadAllowed')
    is_rename_allowed: bool = ApiField(alias='IsRenameAllowed')
    is_revoke_allowed: bool = ApiField(alias='IsRevokeAllowed')
    is_view_allowed: bool = ApiField(alias='IsViewAllowed')
    is_write_allowed: bool = ApiField(alias='IsWriteAllowed')
