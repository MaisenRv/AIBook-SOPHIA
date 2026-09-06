
def make_authors():
    authors = [
        'David Santiago Mancera Robles'
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

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

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

