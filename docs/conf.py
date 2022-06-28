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

project = 'pygieons'
copyright = '2022, pygieons contributors'
author = 'pygieons contributors'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "IPython.sphinxext.ipython_console_highlighting",
    "myst_nb"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

html_theme_options = {
    "single_page": False,
    "repository_url": "https://github.com/pygieons/pygieons/",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_edit_page_button": True,
    "launch_buttons": {
        "binderhub_url": "https://notebooks.gesis.org/binder",
        "thebelab": False,
        "notebook_interface": "jupyterlab",
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# include __init__() in API doc
autoclass_content = 'init'

# Always execute the notebooks to keep the packages on the website up-to-date
jupyter_execute_notebooks = "force"

# Hide title in left navbar
html_title = "Python OS Ecosystem for GIS and Earth Observation"
