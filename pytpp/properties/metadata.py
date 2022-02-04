class MetadataFieldType:
    text_string = 1
    list = 2
    date_time = 4
    identity = 5


class MetadataItem:
    allowed_characters = 'AllowedCharacters'
    allowed_values = 'AllowedValues'
    category = 'Category'
    date_only = 'DateOnly'
    default_values = 'DefaultValues'
    display_after = 'DisplayAfter'
    dn = 'DN'
    error_message = 'ErrorMessage'
    guid = 'Guid'
    help = 'Help'
    localization_table = 'LocalizationTable'
    localized_help = 'LocalizedHelp'
    localized_label = 'LocalizedLabel'
    localized_set = 'LocalizedSet'
    mandatory = 'Mandatory'
    name = 'Name'
    mask = 'Mask'
    maximum_length = 'MaximumLength'
    minimum_length = 'MinimumLength'
    policyable = 'Policyable'
    regular_expression = 'RegularExpression'
    render_hidden = 'RenderHidden'
    render_read_only = 'RenderReadOnly'
    single = 'Single'
    time_only = 'TimeOnly'
    type = 'Type'