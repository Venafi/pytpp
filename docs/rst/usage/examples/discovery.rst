Discovery And Placement
=======================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

.. _placement_usage:

Managing Placement Rules
------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Certificate Placement Rules
    certificate_placement_condiitons = [
        features.placement_rule_condition.common_name.matches_regex('[a-z]*\.(awesome-team\.){0,1}*awesome-domain\.com'),
        features.placement_rule_condition.organizational_unit.contains('Awesome Team')
    ]

    certificate_placement_rule = features.placement_rules.create(
        name='|PlacementRuleName| - Certificate',
        rule_type=AttributeValues.PlacementRules.RuleType.certificate,
        device_location_dn=r'|DevDn|',
        certificate_location_dn=r'|CertDn|',
        conditions=certificate_placement_condiitons
    )

    # SSH Placement Rules
    ssh_placement_conditions = [
        features.placement_rule_condition.hostname.ends_with('awesome-domain.com'),
        features.placement_rule_condition.supports_ssh_v1.is_true()
    ]

    ssh_placement_rule = features.placement_rules.create(
        name='|PlacementRuleName| - SSH',
        rule_type=AttributeValues.PlacementRules.RuleType.ssh,
        device_location_dn=r'|DevDn|',
        conditions=ssh_placement_conditions
    )

.. _network_discovery_usage:

Network Discovery
-----------------

Creating & Deleting Jobs
************************

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate_placement_rule = features.placement_rules.get(name='|PlacementRuleName| - Certificate')
    ssh_placement_rule = features.placement_rules.get(name='|PlacementRuleName| - SSH')

    job = features.discovery.network.create(
        name='Awesome Discovery',
        hosts=[
            '172.168.0.0/16',
            '192.168.123.0/24'
        ],
        ports=[80, 443, 22],  # If empty, the default is used. Check out the default in the source code.
        description='Discovery for certificates and SSH devices in the Awesome Region.',
        contacts=['|LocalUser|', '|DomainUser|'],
        default_certificate_location=r'|OrphanDn|',
        placement_rules=[certificate_placement_rule, ssh_placement_rule]
    )

Scheduling, Unscheduling, And Blacking Out Jobs
***********************************************

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### SCHEDULE ####
    features.discovery.network.schedule(
        job='Awesome Discovery',
        hour=23,                # 24-Hour Format (11 PM) in UTC
        days_of_week=[0, 6],    # Every Saturday and Sunday
        days_of_month=[1, 15],  # The 1st and 15th day of every month
        days_of_year=['5/31']   # May 31st
    )

    #### BLACKOUT ####
    features.discovery.network.blackout_schedule(
        job='Awesome Discovery',
        monday=list(range(1,4)),    # Every Monday from 01:00 thru 04:00 UTC
        thursday=list(range(1, 4))  # Every Thursday from 01:00 thru 04:00 UTC
    )

    #### UNSCHEDULE ####
    features.discovery.network.unschedule(job='Deprecated Job')

Running, Pausing, And Cancelling Jobs
*************************************

.. warning::
    There is a known bug when running jobs using the WebSDK in that the job may actually fail to
    run and will return a "CacheEntryNotFound". There is currently no workaround, so the best
    way to avoid this problem is to schedule the job.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    job = 'Awesome Discovery'
    features.discovery.network.run_now(job=job)
    # Do some stuff...
    if features.discovery.network.is_in_progress(job=job):
        features.discovery.network.pause(job=job)
        # Do some stuff...
        features.discovery.network.resume(job=job)
    try:
        # Wait for 1 hour for the job to complete.
        features.discovery.network.wait_for_job_to_finish(job=job, timeout=(60 * 60))
    except TimeoutError:
        # Kill the job if it is running longer than expected.
        features.discovery.network.cancel(job=job)
        raise
