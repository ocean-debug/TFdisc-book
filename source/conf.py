# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
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
source_suffix = ['.rst', '.md']
exclude_patterns = []

language = 'EN'




