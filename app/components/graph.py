import plotly.graph_objects as go
import plotly.express as px
from secrets import token_urlsafe
from dash import html
from dash import dcc
from dash.html import Div
from pandas import DataFrame
from config import Config

class GraphComponents:
    def candle(df: DataFrame, _id: str = None) -> Div:
        """
        x=df['close_time'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
        """
        candle = go.Figure(
            data=go.Candlestick(
                x=df['close_time'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close']
            )
        ).update_layout(title="Markets - ETH")
        return html.Div(
            children=dcc.Graph(figure=candle),
            id=(_id or f"candlestick-{token_urlsafe(16)}")
        )
