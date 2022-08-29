|Product| Documentation
=======================

The intended audience is anyone having access to the Venafi Trust Protection Platform (TPP) WebSDK API
that is seeking an advanced Python programmable interface to TPP.

|Product| is a programmable interface that leverages the TPP WebSDK. It has layers: the API layer and the
Features layer. The API layer provides serialization and deserialization for using the WebSDK API while the
Features layer serves as an abstraction of the API layer. This allows the programmer to use either the API
layer or the Features layer to accomplish the same task; the Features layer just simplifies everything.

.. _pytpp-requirements:

Requirements
------------

* Python >= 3.8
* Access to an OAuth API Application Integration. You can create a customized API Application Integration in Aperture for PyTPP, which is documented `here <https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creatingNew-Aperture.php>`_. Here is an example JSON that can be uploaded when creating a new API Application Integration in Aperture:

.. code-block:: json

    {
        "id"         : "pytpp",
        "name"       : "Venafi PyTPP SDK",
        "vendor"     : "Venafi, Inc.",
        "description": "Application Integration for PyTPP, a Python interface to TPP.",
        "scope"      : "certificate:approve,delete,discover,manage,read,revoke;ssh:approve,delete,discover,manage,read;codesign:delete,manage,read;configuration:delete,manage,read;restricted:delete,manage,read;security:delete,manage,read;statistics:read;agent:delete,read"
    }

.. note::
    Most PyTPP features require the *configuration:manage* scope to be included in the OAuth Application definition.

Installation
------------

**Using PYPI**

``pip install pytpp``.

**Using GitHub**

``pip install git+https://github.com/Venafi/pytpp.git#egg=pytpp``

Uninstallation
--------------

``pip uninstall -y pytpp``

.. note::
   PyTPP is not versioned with TPP. In fact, PyTPP is meant to be compatible with all supported versions of TPP. There
   are two layers of logic: Features and API. Features abstracts the API to make handy methods for easily accomplishing
   tasks for the user, and being such it can decide which API calls to make based on version compatibility with TPP. The
   API layer, however, is not versioned, and being such it is the developer's responsibility to ensure the API calls made
   to the server are compatible.


.. toctree::
    :hidden:
    :caption: Table Of Contents
    :maxdepth: 1

    rst/usage
    rst/usage/examples
    rst/api_reference
