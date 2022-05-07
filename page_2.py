from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to page 2!')


def create_page_2():
    layout = html.Div([
        nav,
        header,
    ])
    return layout
