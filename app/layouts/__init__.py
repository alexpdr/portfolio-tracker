from ast import Div
from .home import home_layout
from .market import market_layout
import plotly.graph_objects as go
from secrets import token_urlsafe
from plotly.graph_objects import Candlestick
from dash import dcc
from dash import html
from dash.html import Div
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container 
from pandas import DataFrame
from components import Components


class Layouts:
    home = home_layout
    market = market_layout

    @staticmethod
    def base(content: Div) -> Div:
        return html.Div([
            Components.UI.navbar(),
            content,
            html.Div(id="debugger")
        ])
