
def make_authors():
    authors = [
        'David Santiago Mancera Robles',
        'Leidi Johana Garzon Velasquez',
        'Yomar Andrés Romero Polo', 
    ]
    result = ''
    for i in range(len(authors)):
        result += authors[i]
        if i < len(authors) - 1:
            result += ', '
    return result
        

project = 'AIBook-SOPHIA'
copyright = f'2026, {make_authors()}. Licenciado bajo CC BY-NC 4.0'
author = make_authors()
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinxcontrib.tikz'
]

templates_path = ['_templates']
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store', 
    '**/img'
]

language = 'es'

# -- Configuración de LaTeX / MathJax / TikZ ----------------------------------

# Formato de salida para los gráficos TikZ (svg es ultra nítido en web)
tikz_tikzgraph_format = 'svg'
tikz_transparent = True

# Preámbulo de TikZ con la paleta "Deep Tech" y estilos centralizados
tikz_latex_preamble = r"""
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{pagecolor}

% Desactiva el fondo del lienzo en LaTeX
\nopagecolor

% Paleta de Colores "Deep Tech"
\definecolor{AIBlue}{HTML}{1E3A8A}    % Azul marino: Fronteras z = 0, vectores w
\definecolor{AICyan}{HTML}{06B6D4}    % Cían: Entradas x, activaciones
\definecolor{AIRed}{HTML}{E11D48}     % Rojo: Clase 0 / z < 0
\definecolor{AIGreen}{HTML}{10B981}   % Verde: Clase 1 / z > 0
\definecolor{AIGray}{HTML}{64748B}    % Gris: Ejes y grillas

"""

# Atajos de LaTeX y colores para ecuaciones MathJax en HTML
# mathjax3_config = {
#     'tex': {
#         'macros': {
#             'vx': r'\vec{x}',
#             'vw': r'\vec{w}',
#             'sigmoide': r'\sigma(z)',
#         }
#     }
# }

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'
html_theme_options = {
    "navbar_persistent": [],
}

html_title = "AIBook - SOPHIA"
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

