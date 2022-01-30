import dash_bootstrap_components as dbc
from dash import html
from data import Data


class DropdownComponents:

    def symbols(data):
        btc = []
        eth = []
        for composite_symbol in data:
            if composite_symbol.endswith("BTC"):
                symbol = composite_symbol.split("BTC")
                btc.append(dbc.DropdownMenuItem(
                    id=f"dropdown-item-{composite_symbol}",
                    children=f"{symbol[0]}",
                    key=symbol[1],
                    style={"padding": "10px"})
                )
            elif composite_symbol.endswith("ETH"):
                symbol = composite_symbol.split("ETH")
                eth.append(dbc.DropdownMenuItem(
                    id=f"dropdown-item-{composite_symbol}",
                    children=f"{symbol[0]}",
                    key=symbol[1],
                    style={"padding": "10px"})
                )

        return html.Div([
            dbc.DropdownMenu(
                label="BTC", id="dropdown-menu-BTC", children=btc,
                style={"margin": "5px"}
                ),
            dbc.DropdownMenu(
                label="ETH", id="dropdown-menu-ETH", children=eth,
                style={"margin": "5px"}
                )
        ], style={"display": "flex"})

    def timeframes():
        pass
