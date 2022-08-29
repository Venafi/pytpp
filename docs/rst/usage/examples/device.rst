.. _device_usage:

Device
======

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.


Creating And Deleting A Device
------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    device = features.device.create(
        name='|DevName|',
        parent_folder=r'|DevDn|',
        contacts=['|LocalUser|', '|DomainUser|'],
        description='Device description here.',
        address='10.10.15.124',
        agent_provisioning_mode=AttributeValues.Device.ConnectionMethod.agentless,
        concurrent_connection_limit=99,
        device_credential=r'|CredDn|',
        temp_directory='/tmp',
        os_type=AttributeValues.Device.OSType.linux,
        jump_server=f'|DevDn|\|JumpServerName|',
        enforce_host_key=True,
    )

    #### DELETE ####
    features.device.delete(device=device)

Scanning A Device For SSH Keys
------------------------------

.. note::
    1. The device must be part of a client group with SSH Discovery work enabled and assigned to it. See :ref:`client_group_usage`
       for more info.
    2. If the group type is agentless, the device must be in a folder where agentless discovery and remediation is enabled.


.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    features.device.scan_for_ssh_keys(device=r'|DevDn|\|DevName|')
