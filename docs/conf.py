import os
import sys
sys.path += [os.path.abspath('..'), os.path.abspath('../..')]
import re
from pytpp import __version__, __author__
import time

# -- Project information -----------------------------------------------------

project = 'PyTPP'
copyright = time.strftime('%Y, Venafi')
author = __author__
version = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
    'sphinx_rtd_dark_mode',
    'sphinxcontrib.autodoc_pydantic'
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    'style_nav_header_background': 'bottom',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}
default_dark_mode = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]
html_logo = '_static/images/Venafi_LOGO_OrangeWhite_rgb_f.svg'
html_favicon = '_static/images/Venafi_ICON_Orange_rgb_f.svg'

autoclass_content = 'both'
add_module_names = False
autodoc_typehints = 'description'
napoleon_use_ivar = True
napoleon_attr_annotations = True
autodoc_unqualified_typehints = True
autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = False
autodoc_pydantic_validator_list_fields = False
autodoc_pydantic_field_list_validators = False

autodoc_pydantic_model_show_field_summary = False
autodoc_pydantic_model_show_validator_members = False
autodoc_pydantic_model_show_config_summary = False

# region Documentation Variables
string = lambda name, value: f'.. |{name}| replace:: {value}'
link = lambda name, label, href:  f"""
.. |{name}| raw:: html

   <a href="{href}">{label}</a>
"""

doc_variables = [
    string(name='Websdk', value='TPP WebSDK API'),
    string(name='Product', value='PyTPP'),
    link(name='Doc Home Page', label='Venafi TPP WebSDK Documentation', href='https://docs.venafi.com/index.php'),
    link(name='Pydantic Docs', label='Pydantic Documentation', href='https://pydantic-docs.helpmanual.io'),
    link(name='Python Requests library', label='Python Requests library', href='https://docs.python-requests.org/en/latest/'),
    link(name='Venafi Github page', label='Venafi Github page', href='https://github.com/Venafi/pytpp/issues')
]

rst_prolog = '\n'.join(doc_variables) + '\n'
# endregion Documentation Variables

# region Code Block Variables
ca_dn = r'\VED\Policy\Administration\CAs'
ca = 'Awesome CA'

folder = 'Awesome Folder'

cert_dn = r'\VED\Policy\Certificates\Awesome Team'
cert = 'awesome_cert.com'
orppan_dn = r'\VED\Policy\_Orphans'

client_group = 'Awesome Client Group'

client_work = 'Awesome Client Work'

cred_dn = r'\VED\Policy\Administration\Credentials'
cred = 'Awesome Credential'

custom_field_name = 'Awesome Custom Field'

dev_dn = r'\VED\Policy\Installations\Awesome Devices'
dev = 'awesome_device.com'
jump_server = 'awesome_jump_server.com'

appl_dn = fr'{dev_dn}\{dev}'
appl = 'Awesome App'

local_user = 'local:AwesomeUser'
domain_user = 'AD+AwesomeAD:user123'
local_group = 'local:AwesomeGroup'

placement_rule_name = 'Awesome Placement Rule'

wf_dn = r'\VED\Policy\Administration\Workflow'
wf = 'Awesome Workflow'

engine = 'Awesome Engine'

code_block_variables = {
    'AppDn': appl_dn,
    'CaDn': ca_dn,
    'CertDn': cert_dn,
    'CredDn': cred_dn,
    'DevDn': dev_dn,
    'WfDn': wf_dn,
    'AppName': appl,
    'CaName': ca,
    'CertName' : cert,
    'ClientGroupName': client_group,
    'ClientWorkName': client_work,
    'CredName'  : cred,
    'CustomFieldName': custom_field_name,
    'DevName': dev,
    'DomainUser': domain_user,
    'EngineName': engine,
    'FolderName': folder,
    'JumpServerName': jump_server,
    'LocalUser': local_user,
    'LocalGroup': local_group,
    'OrphanDn': orppan_dn,
    'PlacementRuleName': placement_rule_name,
    'WfName'     : wf,
}


# noinspection ALL
def replace_variables_in_code_block(app, docname, source):
    result = source[0]
    for name, value in app.config.code_block_variables.items():
        # noinspection ALL
        result = re.sub('\|(?!\|)' + name + '\|(?!\|)', value.replace('\\', '\\\\'), result)
    source[0] = result


# noinspection ALL
def remove_module_docstring(app, what, name, obj, options, lines):
    if what == "pydantic_model":
        del lines[:]
# endregion Code Block Variables


def setup(app):
    app.add_config_value('code_block_variables', {}, True)
    app.connect('source-read', replace_variables_in_code_block)
    app.connect("autodoc-process-docstring", remove_module_docstring)


def main():
    from pathlib import Path
    from sphinx.application import Sphinx
    from docs.compile_features_documentation import main as compile_docstrings

    compile_docstrings()

    docs_directory = Path('.').absolute()
    source_directory = docs_directory
    configuration_directory = docs_directory
    build_directory = Path(configuration_directory, '_build')
    doctree_directory = Path(build_directory, '.doctrees')
    builder = 'html'

    os.system('make clean')
    app = Sphinx(
        str(source_directory),
        str(configuration_directory),
        str(build_directory),
        str(doctree_directory),
        builder
    )
    app.build(force_all=True)


if __name__ == '__main__':
    main()

