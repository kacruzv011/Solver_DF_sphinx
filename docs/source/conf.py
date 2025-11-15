import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Taller Electrostatica 2D laplace solver'
copyright = '2025, Kevin-Cruz taller_laplace'
author = 'Kevin Andres Cruz Velandia'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']

# 👇👇 ***ESTO ES LO QUE FALTABA***
html_baseurl = "https://kacruzv011.github.io/Solver_DF_sphinx/"

# Para que Furo genere rutas relativas (MUY IMPORTANTE EN GITHUB PAGES)
html_theme_options = {
    "light_logo": "logo.png",   # opcional
    "dark_logo": "logo.png",    # opcional
    "sidebar_hide_name": False,
}

# obligar rutas relativas para que cargue el CSS en GitHub Pages
html_scaled_image_link = False
