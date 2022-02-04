.. _platform_usage:

Platforms
=========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Platform Types
--------------

Refer to :ref:`platforms_feature_list` for the available platform feature types.

Updating Platform Compmonents
-----------------------------

.. code-block:: python

    from pytpp import Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### UPDATE DISCOVERY MANAGER ON SPECIFIC ENGINES ####
    features.platforms.discovery_manager.update_engines(
        engine_names=['|EngineName|-1', '|EngineName|-2'],
        attributes={
            Attributes.platforms.discovery_manager.connection_timeout : ["1"],
            Attributes.platforms.engines.log_debug : ["1"]
        },
    )

Getting The Platforms Root
--------------------------

.. code-block:: python

    from pytpp import Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### GET PLATFORM ROOT ####
    platforms = features.platforms.get()
