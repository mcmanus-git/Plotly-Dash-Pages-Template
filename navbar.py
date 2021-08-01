import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/home'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Page 2", href='/page-2'),
                    dbc.DropdownMenuItem("Page 3", href='/page-3'),
                ],
            ),
        ],
        brand="Home",
        brand_href="/home",
        sticky="top",
        color="dark",
        dark=True,
    )

    return navbar
