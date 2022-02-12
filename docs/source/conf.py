import os
import subprocess
from datetime import date

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:
    subprocess.call('cd ../..; doxygen', shell=True)

# -- Project information -----------------------------------------------------

project = 'Columns UI SDK'
copyright = f'Reupen Shah {date.today().year}'
author = 'Reupen Shah'
language = "en"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'breathe',
    'sphinx_immaterial',
]

breathe_projects = {
    "columns-ui-sdk": "../../doxygen/xml",
}
breathe_default_project = "columns-ui-sdk"
breathe_default_members = ('members', 'undoc-members')
breathe_show_include = False

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_immaterial"


html_theme_options = {
    'site_url':
        'https://yuo.be',
    'repo_url':
        'https://github.com/reupen/columns_ui-sdk/',
    'repo_name':
        'reupen/columns_ui-sdk',
    'repo_type':
        'github',
    'globaltoc_collapse':
        True,
    'features': [
        'navigation.expand',
        # 'navigation.tabs',
        # 'toc.integrate',
        'navigation.sections',
        # 'navigation.instant',
        # 'header.autohide',
        'navigation.top',
        # 'search.highlight',
        # 'search.share',
    ],
    'palette': [
        {
            'media': '(prefers-color-scheme: dark)',
            'scheme': 'slate',
            'primary': 'green',
            'accent': 'light blue',
            'toggle': {
                'icon': 'material/lightbulb',
                'name': 'Switch to light mode',
            },
        },
        {
            'media': '(prefers-color-scheme: light)',
            'scheme': 'default',
            'primary': 'green',
            'accent': 'light blue',
            'toggle': {
                'icon': 'material/lightbulb-outline',
                'name': 'Switch to dark mode',
            },
        },
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
