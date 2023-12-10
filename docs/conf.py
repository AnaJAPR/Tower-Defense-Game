# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../game/"))
sys.path.insert(0, os.path.abspath("../game/assets/audio"))
sys.path.insert(0, os.path.abspath("../game/assets/buttons"))
sys.path.insert(0, os.path.abspath("../game/assets/buttons_images"))
sys.path.insert(0, os.path.abspath("../game/assets/enemies"))
sys.path.insert(0, os.path.abspath("../game/assets/maps"))
sys.path.insert(0, os.path.abspath("../game/assets/menu_audios_images"))
sys.path.insert(0, os.path.abspath("../game/assets/others"))
sys.path.insert(0, os.path.abspath("../game/assets/towers"))


project = 'Tower Defense - A2 LP'
copyright = '2023, Ana Júlia Amaro, Paulo César G. Rodrigues, Guilherme Castilho, Uriel Liann S. G. de Limaima'
author = 'Ana Júlia Amaro, Paulo César G. Rodrigues, Guilherme Castilho, Uriel Liann S. G. de Limaima'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
