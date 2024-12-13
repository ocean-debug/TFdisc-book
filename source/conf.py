# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 1
}

html_static_path = ['_static']

project = 'TFdisc'
copyright = '2024, Haiyang Wang'
author = 'Haiyang Wang'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark',
    'sphinx_markdown_tables']

templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
exclude_patterns = []

language = 'EN'


def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)


