import os
import sys
import django

# Add your Django project to the system path
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'kernel.settings'

django.setup()

project = 'Django-Sage-Qrcode'
copyright = '2024, Radin Ghahremani Sepher Akbarzade'
author = 'Radin Ghahremani Sepher Akbarzade'


# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = []

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']





