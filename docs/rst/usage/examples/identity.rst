.. _identity_usage:

Identity
=============

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

.. note::
    The |Websdk| does not allow for a group or user to be granted special rights such as master admin. These must be
    set manually through the UI.

Users
-----

Creating & Deleting Users
*************************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    # Yep: this guy's name is Awesome Awesome.
    user = features.identity.user.create(
        name='|LocalUser|',
        password='S0m3CrayZP@ssw0rd!',
        email_address='|LocalUser|@awesome-domain.com',
        first_name='Awesome',
        last_name='Awesome'
    )

    #### DELETE ####
    features.identity.user.delete(user=user)

Changing User Passwords
***********************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### CHANGE PASSWORD ####
    user = features.identity.user.set_password(
        user='|LocalUser|',
        new_password='IhateSecurity',
        old_passsword='S0m3CrayZP@ssw0rd!'
    )

Searching Users
***************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### SEARCH MATCHING NAMES ####
    matching_users = features.identity.user.find(
        name='|LocalUser|',
        limit=100
    )
    for user in matching_users:
        print(f'Found a match: {user.name}')

Getting Memberships
*******************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### GET USER MEMBERSHIPS ####
    groups = features.identity.user.get_memberships(identity='|LocalUser|')
    for group in groups:
        print(f'I belong to {group.name}.')

Groups
------

Creating & Deleting Groups
**************************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    group = features.identity.group.create(
        name='|LocalGroup|',
        member_prefixed_names=['|LocalUser|-1', '|LocalUser|-2'],
        get_if_already_exists=True
    )

    #### DELETE ####
    features.identity.group.delete(group=group)

Adding, Getting, & Removing Members
***********************************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### ADD MEMBERS ####
    features.identity.group.add_members(
        group='|LocalGroup|',
        member_prefixed_names=['|LocalUser|-1', '|LocalUser|-2'],
        get_if_already_exists=True
    )

    #### GET MEMBERS ####
    group_members = features.identity.group.get_members(group='|LocalGroup|')

    #### REMOVE MEMBERS ####
    features.identity.group.remove_members(
        group='|LocalGroup|',
        member_prefixed_names=['|LocalUser|-1'],  # Remove just these members.
    )

Searching Users
***************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### SEARCH MATCHING NAMES ####
    matching_groups = features.identity.group.find(
        name='|LocalUser|',
        is_security_group=True,
        is_distribution_group=True,
        limit = 100
    )
    for group in matching_groups:
        print(f'Found a match: {group.name}')

Getting Memberships
*******************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    #### GET GROUP MEMBERSHIPS ####
    groups = features.identity.group.get_memberships(identity='|LocalGroup|')
    for group in groups:
        print(f'I belong to {group.name}.')

Renaming Groups
***************

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api)

    group = feature.identity.group.get(prefixed_name='|LocalGroup|')
    print(f'Old name: {group.name}')

    #### RENAME GROUP ####
    group = features.identity.group.rename(
        group=group,
        new_group_name='|LocalGroup|-1'
    )
    print(f'New group name: {group.name}')
