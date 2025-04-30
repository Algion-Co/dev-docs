# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Developer Documentation'
copyright = '2024, Thomas Gwasira'
author = 'Thomas Gwasira'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_copybutton']
myst_enable_extensions = [
  "colon_fence",
]

templates_path = ['_templates', '_templates/components', '_templates/sections']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_title = project
html_theme = 'theme'
html_theme_path = ["_themes", "_themes/theme"]
html_static_path = ['_static']
# html_additional_pages = {
#     'index': 'test.html',
# }
html_show_sourcelink = False

# Add CSS stylesheets
# def setup(app):
#     app.add_css_file('css/styles.css') # may also be a URL