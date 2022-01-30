import plotly.graph_objects as go
from secrets import token_urlsafe
from plotly.graph_objects import Candlestick
from dash import dcc
from dash import html
from dash.html import Div
import dash_bootstrap_components as dbc
from pandas import DataFrame
from secrets import token_urlsafe
from dash_bootstrap_components import Container

from components import Components
from data import Data


def home_layout() -> Container:
    candle_data = Data.Binance.get_candlestick_data_local()
    symbol_data = Data.Binance.symbols

    return dbc.Container([
        dbc.Row([
            dbc.Col(
                Components.Dropdown.symbols(symbol_data)
            ),
            dbc.Col(
                Components.Graph.candle(candle_data)
            )
        ]),

    ], id="home_header")
