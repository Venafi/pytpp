from pytpp.properties.response_objects.dataclasses import permissions


class Permissions:
    @staticmethod
    def Permissions(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return permissions.Permissions(
            is_associate_allowed=response_object.get('IsAssociateAllowed'),
            is_create_allowed=response_object.get('IsCreateAllowed'),
            is_delete_allowed=response_object.get('IsDeleteAllowed'),
            is_manage_permissions_allowed=response_object.get('IsManagePermissionsAllowed'),
            is_policy_write_allowed=response_object.get('IsPolicyWriteAllowed'),
            is_private_key_read_allowed=response_object.get('IsPrivateKeyReadAllowed'),
            is_private_key_write_allowed=response_object.get('IsPrivateKeyWriteAllowed'),
            is_read_allowed=response_object.get('IsReadAllowed'),
            is_rename_allowed=response_object.get('IsRenameAllowed'),
            is_revoke_allowed=response_object.get('IsRevokeAllowed'),
            is_view_allowed=response_object.get('IsViewAllowed'),
            is_write_allowed=response_object.get('IsWriteAllowed'),
        )
