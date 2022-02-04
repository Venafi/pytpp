from typing import Union
from pytpp.tools.vtypes import Config, Identity
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.properties.response_objects.permissions import Permissions as PermResponseObj


@feature('Permissions')
class Permissions(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def _get_obj_and_identity(self, obj: 'Union[Config.Object, str]', identity: 'Union[Identity.Identity, str]'):
        if isinstance(obj, str):
            obj = self._get_config_object(obj)
        if isinstance(identity, str):
            identity = self._get_identity_object(identity)
        return obj, identity

    def delete(self, obj: 'Union[Config.Object, str]', identity: 'Union[Identity.Identity, str]'):
        """
        Deletes all explicit permissions granted to a user or group on the ``obj``. All implicit permissions,
        i.e. those that are inherited from group memberships and parent folders, are unaffected.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            identity: :ref:`identity_object` or :ref:`prefixed_name` of the user or group.
        """
        obj, identity = self._get_obj_and_identity(obj=obj, identity=identity)
        current_permissions = self.get_explicit(obj=obj, identity=identity)
        if not current_permissions:
            return

        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.delete()
        result.assert_valid_response()

    def get_effective(self, obj: 'Union[Config.Object, str]', identity: 'Union[Identity.Identity, str]'):
        """
        Returns the *effective* permissions of a user or group on the ``obj``. Effective permissions are the
        permissions that are take effect when the user authenticates to TPP. All Master Admin, implicit, and
        explicit permissions are taken into account to evaluate the final effective permissions of a user or group.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            identity: :ref:`identity_object` or :ref:`prefixed_name` of the user or group.

        Returns:
            :py:class:`~.dataclasses.permissions.Permissions`: Effective permissions granted to the ``identity``.
        """
        obj, identity = self._get_obj_and_identity(obj=obj, identity=identity)
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.Effective.get()
        return result.effective_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def get_explicit(self, obj: 'Union[Config.Object, str]', identity: 'Union[Identity.Identity, str]'):
        """
        Returns the `explicit` permissions of a user or group on the ``obj``. Explicit permissions are the
        permissions that are `explicitly` granted to a user or group on a particular object. A user or group may
        have permissions to the object via `implicit` permissions, which are permissions inherited from other
        folders and group memberships. Implicit permissions are ignored. To get implicit permissions, use
        :meth:`~get_implicit`.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            identity: :ref:`identity_object` or :ref:`prefixed_name` of the user or group.

        Returns:
            :py:class:`~.dataclasses.permissions.Permissions`: Explicit permissions granted to the ``identity``.
        """
        obj, identity = self._get_obj_and_identity(obj=obj, identity=identity)
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.get()
        return result.explicit_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def get_implicit(self, obj: 'Union[Config.Object, str]', identity: 'Union[Identity.Identity, str]'):
        """
        Returns the `implicit` permissions of a user or group on the ``obj``. Implicit permissions are permissions
        inherited from other folders and group memberships. To get explicit permissions, use :meth:`get_explicit`.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            identity: :ref:`identity_object` or :ref:`prefixed_name` of the user or group.

        Returns:
            :py:class:`~.dataclasses.permissions.Permissions`: Implicit permissions granted to the ``identity``.
        """
        obj, identity = self._get_obj_and_identity(obj=obj, identity=identity)
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        result = api.get()
        return result.implicit_permissions if result.is_valid_response() else PermResponseObj.Permissions({})

    def list_identities(self, obj: 'Union[Config.Object, str]'):
        """
        Returns a list of Identity objects that have `explicit` permissions to the object. Explicit permissions are the
        permissions that are `explicitly` granted to a user or group on a particular object. A user or group may
        have permissions to the object via `implicit` permissions, which are permissions inherited from other
        folders and group memberships. Implicit permissions are ignored.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.

        Returns:
            List of :ref:`identity_object`.
        """
        obj = self._get_config_object(obj)
        principals = self._api.websdk.Permissions.Object.Guid(obj.guid).get().principals

        principals = [
            self._api.websdk.Identity.Validate.post(identity={'PrefixedUniversal': principal}).identity
            for principal in principals
        ]

        return principals

    def update(self, obj: 'Union[Config.Object, str]', identity: 'Union[Identity.Identity, str]', is_associate_allowed: bool = None,
               is_create_allowed: bool = None, is_delete_allowed: bool = None, is_manage_permissions_allowed: bool = None,
               is_policy_write_allowed: bool = None, is_private_key_read_allowed: bool = None, is_private_key_write_allowed: bool = None,
               is_read_allowed: bool = None, is_rename_allowed: bool = None, is_revoke_allowed: bool = None, is_view_allowed: bool = None,
               is_write_allowed: bool = None):
        """
        Grants the specified permissions to a user or group identity. If any arguments are not specified as
        ``True`` or ``False`` then that value will default to their existing permissions or ``False``.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object.
            identity: :ref:`identity_object` or :ref:`prefixed_name` of the user or group.
            is_associate_allowed: Allows associating/dissociating applications to certificates and pushing certificates
                to the associated applications.
            is_create_allowed: Allows creating subordinate objects to the ``obj``. Also grants View permission.
            is_delete_allowed: Allows deleting subordinate objects to the ``obj``.
            is_manage_permissions_allowed: Allows modification to others' permissions to ``obj`` and its
                subordinate objects.
            is_policy_write_allowed: Allows modification to policy values on folder. Requires View permission. Also grants
                Read and Write permissions.
            is_private_key_read_allowed: Allows download of private keys.
            is_private_key_write_allowed: Allows upload of private keys.
            is_read_allowed: Allows ability to read values on subordinate objects to ``obj``.
            is_rename_allowed: Allows ability to rename and move subordinate objects to ``obj``. Requires Rename
                permission to the destination location.
            is_revoke_allowed: Allows ability to invalidate a certificate. Requires Write permission to the certificate
                object.
            is_view_allowed: Allows ability to view the name of all subordinate objects to ``obj``.
            is_write_allowed: Allows editing of subordinate objects to ``obj``.
        """
        obj, identity = self._get_obj_and_identity(obj=obj, identity=identity)
        if '+' in identity.prefix:
            ptype, pname = identity.prefix.split('+', 1)
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype(ptype).Pname(pname).Principal(identity.universal)
        else:
            api = self._api.websdk.Permissions.Object.Guid(obj.guid).Ptype().Principal(identity.universal)

        current_permissions = self.get_explicit(obj=obj, identity=identity)

        if bool([y for x, y in current_permissions.__dict__.items() if not x.startswith('_') and y is not None]):
            method = api.put
        else:
            method = api.post

        new_permissions = {
            k: v if v is not None else getattr(current_permissions, k) for k, v in dict(
                is_associate_allowed=is_associate_allowed,
                is_create_allowed=is_create_allowed,
                is_delete_allowed=is_delete_allowed,
                is_manage_permissions_allowed=is_manage_permissions_allowed,
                is_policy_write_allowed=is_policy_write_allowed,
                is_private_key_read_allowed=is_private_key_read_allowed,
                is_private_key_write_allowed=is_private_key_write_allowed,
                is_read_allowed=is_read_allowed,
                is_rename_allowed=is_rename_allowed,
                is_revoke_allowed=is_revoke_allowed,
                is_view_allowed=is_view_allowed,
                is_write_allowed=is_write_allowed,
            ).items()
        }

        result = method(**new_permissions)
        result.assert_valid_response()
