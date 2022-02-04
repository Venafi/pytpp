.. _permissions_usage:

Permissions
===========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.


Creating, Updating, & Deleting Permissions
------------------------------------------

.. note::
    Creating and updating permissions use the same method: ``features.permissions.update()``. Updating
    permissions will create them if they do not exist for the user or group.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE/UPDATE ####
    features.permissions.update(
        obj=r'|CaDn|',
        identity='|DomainUser|',
        is_associate_allowed=False,
        is_create_allowed=True,
        is_delete_allowed=True,
        is_manage_permissions_allowed=False,
        is_policy_write_allowed=False,
        is_private_key_read_allowed=False,
        is_private_key_write_allowed=False,
        is_read_allowed=True,
        is_rename_allowed=True,
        is_revoke_allowed=False,
        is_view_allowed=True,
        is_write_allowed=True
    )

    #### DELETE ####
    features.permissions.delete(
        obj=r'|CertDn|',
        identity='|DomainUser|'
    )

Getting Explicit Permissions
----------------------------

.. note::
    Explicit permissions are the permissions that are *explicitly* granted to a user or group on the object.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### GET EXPLICIT PERMISSIONS ####
    permissions = feature.permissions.get_explicit(
        obj=r'|CertDn|',
        identity='|DomainUser|',
    )

Getting Implicit Permissions
----------------------------

.. note::
    Implicit permissions are permissions inherited from other folders and group memberships.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    permissions = feature.permissions.get_implicit(
        obj=r'|CaDn|',
        identity='|DomainUser|',
    )

Getting Effective Permissions
-----------------------------

.. note::
    Effective permissions are the permissions that are *effectively* enforced by TPP. All master admin, implicit,
    and explicit permissions are taken into account to evaluate the final effective permissions of a user or group.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    permissions = feature.permissions.get_effective(
        obj=r'|CaDn|',
        identity='|DomainUser|',
    )

Listing Identities Permitted On An Object
-----------------------------------------

.. note::
    Identites returned are those having *effective* permissions on the object.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### LIST ALL IDENTITY PERMISSIONS ####
    identities = feature.permissions.list_identities(obj=r'|CaDn|')

    for identity in identities:
        print(identity.name)
