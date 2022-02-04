.. _client_work_usage:

Client Work
===========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

.. note::
    The feature for client work is implemented by making use of the WebSDK Config API. It is a wrapper around that API
    to make interacting with client work easier.

Client Work Types
-----------------

Refer to :ref:`client_work_feature_list` for the available client work feature types.

.. note::
    When assigning client work to a client group, not all client work types can be assigned to all client group types.
    See :ref:`client_groups_feature_list` for more information.

Creating & Deleting Client Work
-------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    client_work = features.client_work.ssh_remediation.create(name='|ClientWorkName|')

    #### DELETE ####
    features.client_work.ssh_remediation.delete(work=client_work)

Scheduling & Unscheduling Client Work
-------------------------------------

.. note::
    Every client work type has different scheduling options. Refer to :ref:`client_work_feature_list` for more info.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='|ClientWorkName|')

    #### SCHEDULE ####
    features.client_work.ssh_remediation.schedule(work=client_work, start_time=2, daily=True)

    #### UNSCHEDULE ####
    features.client_work.ssh_remediation.unschedule(work=client_work)

Enabling & Disabling Client Work
--------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    client_work = features.client_work.ssh_remediation.create(name='|ClientWorkName|')

    #### ENABLE ####
    features.client_work.ssh_remediation.enable(work=client_work)

    #### DISABLE ####
    features.client_work.ssh_remediation.disable(work=client_work)

Listing All Client Work By Type
-------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    all_client_work = features.client_work.ssh_remediation.list()

    for client_work in all_client_work:
        print(client_work.name)
