from typing import List, Union
from pytpp.tools.vtypes import Config
from pytpp.properties.config import PlacementRulesAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.attributes.layout_rule_base import LayoutRuleBaseAttributes


@feature('Placement Rule Condition')
class PlacementRuleCondition:
    @property
    def city(self):
        """Base condition on the certificate city value."""
        return self._Operators(field='Certificate.City')

    @property
    def common_name(self):
        """Base condition on the certificate common name value."""
        return self._Operators(field='Certificate.CN')

    @property
    def country(self):
        """Base condition on the certificate country value."""
        return self._Operators(field='Certificate.C')

    @property
    def domain_component(self):
        """Base condition on the certificate domain component value."""
        return self._Operators(field='Certificate.DC')

    @property
    def expired(self):
        """Base condition on the certificate expiration value."""
        return self._Operators(field='Certificate.Expired')

    @property
    def hostname(self):
        """Base condition on the discovered hostname value."""
        return self._Operators(field='Discovery.Hostname')

    @property
    def ip_address(self):
        """Base condition on the discovered IP Address value."""
        return self._Operators(field='Discovery.Address')

    @property
    def issuer_dn(self):
        """Base condition on the certificate issuer :ref:`dn` value."""
        return self._Operators(field='Certificate.Issuer')

    @property
    def operating_system(self):
        """Base condition on the discovered Operating System value."""
        return self._Operators(field='Discovery.OS')

    @property
    def organization(self):
        """Base condition on the certificate organization value."""
        return self._Operators(field='Certificate.O')

    @property
    def organizational_unit(self):
        """Base condition on the certificate organizational unit value."""
        return self._Operators(field='Certificate.OU')

    @property
    def port(self):
        """Base condition on the discovered port value."""
        return self._Operators(field='Discovery.Port')

    @property
    def san(self):
        """Base condition on the certificate SAN DNS value."""
        return self._Operators(field='Certificate.SANDNS')

    @property
    def self_signed(self):
        """Base condition on whether or not the certificate is self-signed."""
        return self._Operators(field='Certificate.SelfSigned')

    @property
    def server_version(self):
        """Base condition on the SSH server version value."""
        return self._Operators(field='SSH.ServerVersion')

    @property
    def state(self):
        """Base condition on the certificate state value."""
        return self._Operators(field='Certificate.State')

    @property
    def supports_ssh_v1(self):
        """Base condition on if the target supports SSH V1."""
        return self._Operators(field='SSH.Version', force_value='1')

    @property
    def supports_ssh_v2(self):
        """Base condition on if the target supports SSH V2."""
        return self._Operators(field='SSH.Version', force_value='2')

    class _Operators:
        def __init__(self, field: str, force_value: str = None):
            self._field = field
            self._forced_value = force_value

        def matches(self, value: str):
            """
            Args:
                value: String to match.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} == "{value}"'

        def in_list(self, values: List[str]):
            """
            Args:
                values: List of strings to match.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f"{self._field} in [{','.join(map(str, values))}]"

        def starts_with(self, value: str):
            """
            Args:
                value: String that the target field's value begins with.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} > "{value}"'

        def ends_with(self, value: str):
            """
            Args:
                value: String that the target field's value ends with.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} < "{value}"'

        def contains(self, value: str):
            """
            Args:
                value: String within the target field's value.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} like "{value}"'

        def matches_regex(self, value: str):
            """
            Args:
                value: String to match by regular expression.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} @= "{value}"'

        def is_true(self):
            """
            Returns: Condition string for the Placement Rule to be created.
            """
            if self._forced_value:
                return f"{self._field} == {self._forced_value}"
            return f"{self._field} == 1"

        def is_false(self):
            """
            Returns: Condition string for the Placement Rule to be created.
            """
            if self._forced_value:
                return f"{self._field} != {self._forced_value}"
            return f"{self._field} == 0"


@feature('Placement Rules')
class PlacementRules(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._layout_rules_dn = r'\VED\Layout Root\Rules'

    def _format_rule_attribute(self, conditions: List[str], device_location: 'Union[Config.Object, str]',
                               certificate_location: 'Union[Config.Object, str]' = None,
                               rule_type: str = 'X509 Certificate'):
        """
        Formats the rule attribute on the Placement Rule object.
        """
        context = 'CONTEXT\n\tDiscovery'
        rule_types = f"FOR\n\t{','.join(('Device', rule_type))}"
        conditions = f"IF\n\t{' && '.join(conditions)}"
        locations = [f'Location[Device]={self._get_dn(device_location)}']
        if certificate_location:
            locations.append(f'Location[X509 Certificate Base]={self._get_dn(certificate_location)}')
        locations = f"THEN\n\t" + '\n\t'.join(locations)

        return f"{context}\n{rule_types}\n{conditions}\n{locations}\nEND"

    def create(self, name: str, conditions: List[str], device_location: 'Union[Config.Object, str]',
               certificate_location: 'Union[Config.Object, str]' = None, rule_type: str = 'X509 Certificate',
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the placement rule.
            conditions: A list of strings that define the conditions of the rule. Use :class:`PlacementRuleCondition` to 
                        create the rule conditions. See :ref:`placement_usage` for examples.
            device_location: :ref:`config_object` or :ref:`dn` of the folder in which to place applicable devices.
            certificate_location: :ref:`config_object` or :ref:`dn` of the folder in which to place applicable certificates.
            rule_type: Default is 'X509 Certificate'. 'SSH' may be specified instead for SSH discovery.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the placement rule object.
        """
        rule_attr = self._format_rule_attribute(
            conditions=conditions,
            device_location=device_location,
            certificate_location=certificate_location,
            rule_type=rule_type
        )
        rule = self._config_create(
            name=name,
            parent_folder_dn=self._layout_rules_dn,
            attributes={
                LayoutRuleBaseAttributes.rule: rule_attr
            },
            config_class=LayoutRuleBaseAttributes.__config_class__,
            get_if_already_exists=get_if_already_exists
        )
        return rule

    def delete(self, rule: 'Union[Config.Object, str]'):
        """
        Deletes a placement rule.

        Args:
            rule: :ref:`config_object` or name of the placement rule.
        """
        rule_dn = self._get_dn(rule, parent_dn=self._layout_rules_dn)
        response = self._config_delete(object_dn=rule_dn)
        response.assert_valid_response()

    def update(self, rule: 'Union[Config.Object, str]', conditions: List[str] = None, device_location: str = None,
               certificate_location: str = None, rule_type: str = 'X509 Certificate'):
        """
        Updates a placement rule. If certain parameters are not provided, the current parameters will be rewritten
        to the object. In other words, only the parameters given are updated.

        Args:
            rule: :ref:`config_object` or name of the placement rule.
            conditions: A list of strings that define the conditions of the rule. Use :class:`PlacementRuleCondition` to
                        create the rule conditions. See :ref:`placement_usage` for examples.
            device_location: :ref:`config_object` or :ref:`dn` of the folder in which to place applicable devices.
            certificate_location: :ref:`config_object` or :ref:`dn` of the folder in which to place applicable certificates.
            rule_type: Default is 'X509 Certificate'. 'SSH' may be specified instead for SSH discovery.
        """
        rule_dn = self._get_dn(rule, parent_dn=self._layout_rules_dn)
        current_attr = self._api.websdk.Config.Read.post(
            object_dn=rule_dn,
            attribute_name=LayoutRuleBaseAttributes.rule
        ).values[0]
        new_conditions = conditions or []
        new_certificate_dn = self._get_dn(certificate_location) if certificate_location else ''
        new_device_dn = self._get_dn(device_location) if device_location else ''
        get_conditions = get_locations = False
        for line in current_attr.splitlines():
            if line.strip() == 'IF':
                if not conditions:
                    get_conditions = True
                get_locations = False
            elif line.strip() == 'THEN':
                get_conditions = False
                if not(new_certificate_dn and new_device_dn):
                    get_locations = True
            elif line.strip() == 'END':
                break
            elif get_conditions:
                new_conditions = line.strip().split(' && ')
                get_conditions = False
            elif get_locations:
                if 'Location[Device]' in line and not new_device_dn:
                    new_device_dn = line.split('=', 1)[-1].strip()
                elif 'Location[X509 Certificate Base]' in line and not new_certificate_dn:
                    new_certificate_dn = line.split('=', 1)[-1].strip()

        if rule_type == PlacementRulesAttributeValues.RuleType.ssh:
            new_certificate_dn = None

        rule_attr = self._format_rule_attribute(
            conditions=new_conditions,
            device_location=new_device_dn,
            certificate_location=new_certificate_dn,
            rule_type=rule_type
        )
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=rule_dn,
            attribute_name=LayoutRuleBaseAttributes.rule,
            values=[
                rule_attr
            ]
        )
        response.assert_valid_response()

    def get(self, name: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            name: Name of the placement rule.
            raise_error_if_not_exists: Raise an exception if the placement rule does not exist.

        Returns:
            :ref:`config_object` of the placement rule object.
        """
        return self._get_config_object(
            object_dn=f'{self._layout_rules_dn}\\{name}',
            raise_error_if_not_exists=raise_error_if_not_exists
        )
