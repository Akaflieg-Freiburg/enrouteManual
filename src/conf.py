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


# -- Project information -----------------------------------------------------

project = 'Enroute Flight Navigation'
copyright = '2024, Stefan Kebekus'
author = 'Stefan Kebekus'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = ['sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


#
# Options for HTML output
#

html_favicon = "de.akaflieg_freiburg.enroute.png"
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
}


#
# Options for LaTeX output
#

latex_docclass = {
    'manual': 'scrreprt',
}
latex_elements = {
    'fncychap': '',
    'fontpkg': r'\usepackage{libertine}',
    'maketitle': r'\maketitle',
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'\input{../../latexPreamble.tex.txt}',
}
