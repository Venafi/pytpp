from dataclasses import dataclass


@dataclass
class Permissions:
    is_associate_allowed: bool
    is_create_allowed: bool
    is_delete_allowed: bool
    is_manage_permissions_allowed: bool
    is_policy_write_allowed: bool
    is_private_key_read_allowed: bool
    is_private_key_write_allowed: bool
    is_read_allowed: bool
    is_rename_allowed: bool
    is_revoke_allowed: bool
    is_view_allowed: bool
    is_write_allowed: bool
