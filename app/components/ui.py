
import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_components import NavbarSimple
from config import Config


class UIComponents:
    def navbar() -> NavbarSimple:
        return dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Market", href="#")),
                dbc.NavItem(dbc.NavLink("Trade", href="#")),
                dbc.NavItem(dbc.NavLink("Wallet", href="#")),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("...", header=True),
                        dbc.DropdownMenuItem("Page 2", href="#"),
                        dbc.DropdownMenuItem("Page 3", href="#"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="More",
                ),
            ],
            brand=f"{Config().App.name}",
            brand_href="#",
            color="primary",
            dark=True,
        )
