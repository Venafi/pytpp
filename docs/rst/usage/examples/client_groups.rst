.. _client_group_usage:

Client Group
============

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.


.. note::
    The feature for client groups is implemented by making use of the WebSDK Config API. It is a wrapper around that API
    to make interacting with client groups easier.

Client Group Types
------------------

Refer to :ref:`client_groups_feature_list` for the available client group feature types.

Creating & Deleting A Client Group
----------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    client_group = features.client_groups.agentless.create(name='|ClientGroupName|')

    #### DELETE ####
    features.client_groups.delete(group=client_group)

Assigning & Removing Client Work
--------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### ASSIGN CLIENT WORK ####
    features.client_groups.agentless.assign_work(group='|ClientGroupName|', work='|ClientWorkName|')

    #### REMOVE CLIENT WORK ####
    features.client_groups.remove_work(group='|ClientGroupName|', work='|ClientWorkName|')

Listing All Client Groups
-------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    all_client_groups = features.client_groups.list()

    for client_group in all_client_groups:
        print(client_group.name)
