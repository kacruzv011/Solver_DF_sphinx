import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Taller Electrostatica'
copyright = '2023, Estudiante Taller Avanzado'
author = 'Estudiante Taller Avanzado'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
