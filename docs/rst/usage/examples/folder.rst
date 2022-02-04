.. _folder_usage:

Folder
======

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.


Creating And Deleting A Folder
------------------------------

.. warning::
    Deleting a folder will also remove all objects from its associated secrets, such as private key information
    stored in the database. While the opbject is removed from the secret, the secret is not removed from the
    vault until the secret has no other associations to it, in which case the secret will be removed. If you
    wish to preserve the object's association to it secrets use the WebSDK API ``POST Config/Delete`` instead.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    folder = features.folder.create(
        name='|FolderName|',
        parent_folder=r'|CertDn|',
        description='Folder description here.',
        contacts=['LocalUser', 'DomainUser'],
        engines=['|EngineName|-1', '|EngineName|-2'],
        log_server='|EngineName|-1 Log Server',
    )

    #### DELETE ####
    features.folder.delete(folder=folder, recursive=True)

Getting, Adding And Removing Engines
------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### SET PROCESSING ENGINES ####

    # Add these two engines as the processing engines for this folder. All other
    # engines will be removed.
    features.folder.set_engines(
        folder=r'|CertDn|\|FolderName|',
        engines=['|EngineName|-1', '|EngineName|-2'],
        append_engines=False  # Set to "True" to preserve existing engines.
    )

    #### GET PROCESSING ENGINES ####
    engines = features.folder.get_engines(folder=r'|CertDn|\|FolderName|')
    print([e.engine_name for e in engines])  # prints "['|EngineName|-1', '|EngineName|-2']"

    #### REMOVE PROCESSING ENGINES ####

    # Remove all engines from the folder. Now all engines will be able to process work from
    # this folder.
    features.folder.delete_engines(folder=r'|CertDn|\|FolderName|')

.. _applying_workflows:

Applying And Removing Workflows
-------------------------------

.. rubric:: Managing Applied Workflows
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### APPLY WORKFLOW ####
    features.folder.apply_workflow(
        folder=r'|CertDn|\|FolderName|',
        workflow=r'|WfDn|\|WfName|'
    )

    #### REMOVE WORKFLOW ####
    features.folder.remove_workflow(
        folder=r'|CertDn|\|FolderName|',
        workflow=r'|WfDn|\|WfName|'
    )

.. rubric:: Managing Blocked Workflows
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### ADD BLOCKING WORKFLOW ####
    features.folder.block_workflow(
        folder=r'|CertDn|\|FolderName|',
        workflow=r'|WfDn|\|WfName|'
    )

    #### REMOVE BLOCKING WORKFLOW ####
    features.folder.remove_blocked_workflow(
        folder=r'|CertDn|\|FolderName|',
        workflow=r'|WfDn|\|WfName|'
    )

Searching Objects
-----------------

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    #### SEARCH FOLDER ####
    items = features.folder.search(
        object_name_pattern='*awesome-domain?.com',
        object_types=[Attributes.certificate.__config_class__, Attributes.device.__config_class__],
        starting_dn=r'|CertDn|\|FolderName|',
        recursive=True
    )

    # prints the DN of all "X509 Certificate" and "Device" items found recursively under
    # the "starting_dn".
    print([i.dn for i in items])

Managing Policies
-----------------

.. _read_policy_attributes:

.. rubric:: Reading Policy Attributes

.. note::
    Reading policy values on a folder only returns the policy values *set* on that folder and not the
    effective value (that may be inherited by a parent policy). To read the *effective* policy value
    use :ref:`read_attributes`.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    #### READ POLICY VALUES ####
    values, locked = features.folder.read_policy(
        folder=r'|CertDn|\|FolderName|',
        class_name=Attributes.certificate.__config_class__,
        attribute_name=Attributes.certificate.certificate_authority
    )

.. _write_policy_attributes:

.. rubric:: Writing Policy Attributes

.. note::
    When writing policy values (as opposed to updating them) the current value(s) will be
    overwritten. To simply update the value(s) refer to :ref:`update_policy_attributes`.


.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    #### WRITE POLICY VALUES ####
    features.folder.write_policy(
        folder=r'|CertDn|\|FolderName|',
        class_name=Attributes.certificate.__config_class__,
        attributes={
            Attributes.certificate.approver: ['|LocalUser|', '|DomainUser|']
        },
        locked=True
    )

.. _update_policy_attributes:

.. rubric:: Updating Policy Attributes

.. note::
    When updating policy values (as opposed to writing them) the current value(s) will *not*
    be overwritten, but will be appended by the requested value(s). To overwrite the existing
    value(s) refer to :ref:`write_policy_attributes`.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    #### UPDATE POLICY VALUES ####
    features.folder.update_policy(
        folder=r'|CertDn|\|FolderName|',
        class_name=Attributes.certificate.__config_class__,
        attributes={
            Attributes.certificate.approver: ['|LocalUser|', '|DomainUser|']
        },
        locked=True
    )

.. rubric:: Clearing Policy Attributes

.. note::
    There are two options when clearing a policy attribute, determined by the type of the attributes parameter.

    * ``Dictionary``: The key is the attribute name and the value is a list of values to be removed. If no values
      remain for the attribute then the attribute is removed.
    * ``List``: All items are attribute names that are to be removed from the object entirely.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    #### CLEAR WITH DICTIONARY ####

    # Clear only one approver on the policy, but preserve the rest that may exist.
    features.folder.clear_policy(
        folder=r'|CertDn|\|FolderName|',
        class_name=Attributes.certificate.__config_class__,
        attributes={
            Attributes.certificate.approver: ['|LocalUser|']
        }
    )

    #### CLEAR WITH LIST ####

    # Clear all approvers on the policy.
    features.folder.clear_policy(
        folder=r'|CertDn|\|FolderName|',
        class_name=Attributes.certificate.__config_class__,
        attributes=[
            Attributes.certificate.approver
        ]
    )
