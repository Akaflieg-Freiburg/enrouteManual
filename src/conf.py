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
    'preamble': r'\input{../../src/latexPreamble.tex.txt}',
}


#
# WebP conversion of content images (HTML builder only)
#
# The manual ships inside the enroute app package, where size matters. Sphinx
# writes all content images (figure::/image::) to _images/ as PNG; after the
# HTML build we transcode them to WebP (~88% smaller, measured) and rewrite the
# <img> references. The manual is shown in a native WebView on every platform,
# all of which decode WebP, so the app side needs no change. LaTeX/PDF output is
# untouched -- the hook is guarded on the html builder.

import os
import subprocess


def _pngs_to_webp(app, exception):
    if exception is not None or app.builder.name != 'html':
        return
    images_dir = os.path.join(app.outdir, '_images')
    if not os.path.isdir(images_dir):
        return
    renamed = {}
    for name in sorted(os.listdir(images_dir)):
        if not name.lower().endswith('.png'):
            continue
        png = os.path.join(images_dir, name)
        webp_name = name[:-4] + '.webp'
        subprocess.run(
            ['cwebp', '-quiet', '-q', '80', '-m', '6', '-sharp_yuv',
             png, '-o', os.path.join(images_dir, webp_name)],
            check=True,
        )
        os.remove(png)
        renamed[name] = webp_name
    # Rewrite _images/<name>.png -> _images/<name>.webp in the generated HTML.
    # Only the _images/NAME.png tail is replaced, so any '../' prefix from
    # sub-pages is preserved.
    for root, _dirs, files in os.walk(app.outdir):
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            with open(path, encoding='utf-8') as fh:
                html = fh.read()
            new = html
            for png_name, webp_name in renamed.items():
                new = new.replace('_images/' + png_name, '_images/' + webp_name)
            if new != html:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(new)


def setup(app):
    app.connect('build-finished', _pngs_to_webp)
