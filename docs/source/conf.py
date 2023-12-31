import os
import sys
from pprint import pprint

# Configuration file for the Sphinx documentation builder.
# -- Project information
project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'
release = '0.1'
version = '0.1.0'

# -- General configuration
sys.path.insert(0, os.path.abspath(r'../../'))
sys.path.insert(0, os.path.abspath(r'../'))
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'bizstyle'

# -- Options for EPUB output
epub_show_urls = 'footnote'

pprint(sys.path)
