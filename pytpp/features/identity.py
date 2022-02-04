from pytpp.attributes.user import UserAttributes
from pytpp.properties.config import IdentityAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import UnexpectedValue
from pytpp.features.definitions.classes import Classes
from typing import List, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Identity


class _IdentityBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._identity_dn = r'\VED\Identity'

    def _find(self, name: str, limit: int = 100, is_distribution_group: bool = False, is_security_group: bool = False,
              is_user: bool = False):
        identity_type = 0
        if is_user:
            identity_type += IdentityAttributeValues.Types.user
        if is_security_group:
            identity_type += IdentityAttributeValues.Types.security_group
        if is_distribution_group:
            identity_type += IdentityAttributeValues.Types.distribution_group

        result = self._api.websdk.Identity.Browse.post(
            filter=name,
            limit=limit,
            identity_type=identity_type
        )
        return result.identities

    def exists(self, prefixed_name: str):
        """
        Args:
            prefixed_name: The :ref:`prefixed_name` of the identity.

        Returns:
            bool: ``True`` if the identity exists, otherwise ``False``.
        """
        response = self._api.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name)
        )
        response.assert_valid_response()
        if response.api_response.content:
            return response.identity.prefixed_name == prefixed_name
        return False

    def get(self, prefixed_name: str = None, prefixed_universal: str = None, raise_error_if_not_exists: bool = True):
        """
        One of ``prefixed_name`` or ``prefixed_universal`` must be provided.

        Args:
            prefixed_name: The :ref:`prefixed_name` of the identity object.
            prefixed_universal: The prefixed universal of the identity object.
            raise_error_if_not_exists: Raise an exception if the identity does not exist.

        Returns:
           :ref:`identity_object`
        """
        return self._get_identity_object(
            prefixed_name=prefixed_name,
            prefixed_universal=prefixed_universal,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def get_memberships(self, identity: 'Union[Identity.Identity, str]'):
        """
        Args:
            identity: :ref:`identity_object` or :ref:`prefixed_name` of the identity.

        Returns:
            List of :ref:`identity_object` for each group.
        """
        if isinstance(identity, str):
            identity = self._get_identity_object(prefixed_name=identity)
        memberships = self._api.websdk.Identity.GetMemberships.post(
            identity=self._identity_dict(
                prefixed_name=identity.prefixed_name,
                prefixed_universal=identity.prefixed_universal
            )
        ).identities

        return memberships

    def read_attribute(self, identity: 'Union[Identity.Identity, str]', attribute_name: str):
        """
        Args:
            identity: :ref:`identity_object` or :ref:`prefixed_name` of the identity.
            attribute_name: The name of the attribute.

        Returns:
            List[str]: List of attribute values.
        """
        prefixed_name = self._get_prefixed_name(identity)
        result = self._api.websdk.Identity.ReadAttribute.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            attribute_name=attribute_name
        )
        return result.attributes


@feature('User')
class User(_IdentityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, password: str, email_address: str, first_name: str = None, last_name: str = None,
               add_to_everyone_group: bool = True, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the user. The *local:* prefix is not required.
            password: Password.
            email_address: E-mail address.
            first_name: First name of the user.
            last_name: Last name of the user.
            add_to_everyone_group: Add the user to the ``local:Everyone`` group.
            get_if_already_exists: If the identity already exists, just return it as is.

        Returns:
            :ref:`identity_object` of the user.
        """
        attributes = {
            UserAttributes.internet_email_address: email_address,
            UserAttributes.given_name: first_name,
            UserAttributes.surname: last_name
        }
        user = self._config_create(
            name=name,
            parent_folder_dn=self._identity_dn,
            config_class=Classes.user,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )
        user = self.set_password(user=f'local:{user.name}', new_password=password)

        if add_to_everyone_group:
            response = self._api.websdk.Identity.AddGroupMembers.put(
                group=self._identity_dict(prefixed_name='local:Everyone'),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            response.assert_valid_response()
        return user

    def delete(self, user: 'Union[Identity.Identity, str]'):
        """
        Deletes the user from the Local Identity Provider. The user is removed from all local groups.

        Args:
            user: :ref:`identity_object` or :ref:`prefixed_name` of the user.
        """
        if isinstance(user, str):
            user = self._get_identity_object(user)
        groups = self.get_memberships(identity=user)
        for group in groups:
            result = self._api.websdk.Identity.RemoveGroupMembers.put(
                group=self._identity_dict(prefixed_name=group.prefixed_name),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            result.assert_valid_response()
        self._config_delete(object_dn=f'{self._identity_dn}\\{user.name}')

    def find(self, name: str, limit: int = 100):
        """
        Finds users within the the Identity Providers to which the authenticated user has view permissions.
        
        Args:
            name: String of characters contained within the names to be found.
            limit: Maximum number of results to return.

        Returns:
            List of :ref:`identity_object` for each user found.
        """
        return self._find(
            name=name,
            limit=limit,
            is_distribution_group=False,
            is_security_group=False,
            is_user=True
        )

    def set_password(self, user: 'Union[Identity.Identity, str]', new_password: str, old_password: str = None):
        """
        Sets the ``new_password`` for a local user. If the user did not have a previous password, then
        the ``old_password`` is not required.

        Args:
            user: :ref:`identity_object` or :ref:`prefixed_name` of the user.
            new_password: The new password for the user.
            old_password: The old password for the user. Required only if it exists.

        Returns:
            :ref:`identity_object` of the user.
        """
        prefixed_name = self._get_prefixed_name(user)
        response = self._api.websdk.Identity.SetPassword.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            old_password=old_password,
            password=new_password
        )
        return response.identity


@feature('Group')
class Group(_IdentityBase):
    def __init__(self, api):
        super().__init__(api=api)

    def add_members(self, group: 'Union[Identity.Identity, str]', members: 'List[Union[Identity.Identity, str]]'):
        """
        Args:
            group: :ref:`identity_object` or :ref:`prefixed_name` of the group.
            members: List of :ref:`identity_object` or :ref:`prefixed_name` of each member.

        Returns:
            List of :ref:`identity_object` for each member.
        """
        member_prefixed_names = [self._get_prefixed_name(i) for i in members]
        prefixed_name = self._get_prefixed_name(group)
        result = self._api.websdk.Identity.AddGroupMembers.put(
            group=self._identity_dict(prefixed_name=prefixed_name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ],
            show_members=True
        )

        if member_prefixed_names and result.invalid_members:
            im = "\n\t".join([m.prefixed_name for m in result.invalid_members])
            raise UnexpectedValue(
                f'Unable to add these members to the group "{prefixed_name}":\n\t{im}'
            )

        return result.members

    def create(self, name: str, members: 'List[Union[Identity, Identity, str]]' = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the user. The *local:* prefix is not required.
            members: List of :ref:`identity_object` or :ref:`prefixed_name` of each member.
            get_if_already_exists: If the identity already exists, just return it as is.

        Returns:
            :ref:`identity_object` of the group.
        """
        member_prefixed_names = [self._get_prefixed_name(i) for i in members] if members else []
        if not name.startswith('local:'):
            name = f'local:{name}'
        if get_if_already_exists:
            if self.exists(prefixed_name=name):
                return self.get(prefixed_name=name)

        result = self._api.websdk.Identity.AddGroup.post(
            name=self._identity_dict(prefixed_name=name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ]
        )

        if member_prefixed_names and result.invalid_members:
            im = "\n\t".join([m.prefixed_name for m in result.invalid_members])
            self._log_warning_message(
                msg=f'Unable to add these members to the group "{name}":\n\t{im}'
            )

        group = result.identity
        return group

    def delete(self, group: 'Union[Identity.Identity, str]'):
        """
        Deletes a group, but not its members. All group permissions and privileges are deleted.

        Args:
            group: :ref:`identity_object` or :ref:`prefixed_name` of the group.
        """
        if isinstance(group, str):
            group = self._get_identity_object(group)
        result = self._api.websdk.Identity.Group.Prefix(group.prefix).Principal(group.universal).delete()
        result.assert_valid_response()

    def find(self, name: str, limit: int = 100, is_distribution_group: bool = False, is_security_group: bool = True):
        """
        Finds groups within the the Identity Providers to which the authenticated user has view permissions.

        Args:
            name: String of characters contained within the names to be found.
            limit: Maximum number of results to return.
            is_distribution_group: If ``True``, results include AD Distribution Groups.
            is_security_group: If ``True``, results include Local and AD/LDAP groups.

        Returns:
            List of :ref:`identity_object` for each group found.
        """
        return self._find(
            name=name,
            limit=limit,
            is_distribution_group=is_distribution_group,
            is_security_group=is_security_group,
            is_user=False
        )

    def get_members(self, group: 'Union[Identity.Identity, str]', resolve_nested: bool = False):
        """
        Args:
            group: :ref:`identity_object` or :ref:`prefixed_name` of the group.
            resolve_nested: If ``True``, recursively returns members of groups within this group.

        Returns:
            List of :ref:`identity_object` for each member of the group.
        """
        prefixed_name = self._get_prefixed_name(group)
        result = self._api.websdk.Identity.GetMembers.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            resolve_nested=int(resolve_nested)
        )

        return result.identities

    def remove_members(self, group: 'Union[Identity.Identity, str]', members: 'List[Union[Identity.Identity, str]]'):
        """
        Removes members from a local group.

        Args:
            group: :ref:`identity_object` or :ref:`prefixed_name` of the group.
            members: List of :ref:`identity_object` or :ref:`prefixed_name` of each member.

        Returns:
            List of :ref:`identity_object` for each remaining member. If no members remain, then
            the list is empty.
        """
        member_prefixed_names = [self._get_prefixed_name(i) for i in members]
        prefixed_name = self._get_prefixed_name(group)
        result = self._api.websdk.Identity.RemoveGroupMembers.put(
            group=self._identity_dict(prefixed_name=prefixed_name),
            members=[
                self._identity_dict(prefixed_name=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ],
            show_members=True
        )

        return result.members

    def rename(self, group: 'Union[Identity.Identity, str]', new_group_name: str):
        """
        Renames a local group. The *local:* prefix is not required.

        Args:
            group: :ref:`identity_object` or :ref:`prefixed_name` of the group.
            new_group_name: New name of the group. No prefix required.

        Returns:
            :ref:`identity_object` with the new group name.
        """
        prefixed_name = self._get_prefixed_name(group)
        if not new_group_name.startswith('local:'):
            new_group_name = new_group_name.lstrip('local:')

        result = self._api.websdk.Identity.RenameGroup.put(
            group=self._identity_dict(prefixed_name=prefixed_name),
            new_group_name=new_group_name
        )

        return result.identity
