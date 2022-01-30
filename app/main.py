import dash
import plotly.graph_objects as go
from dash import dcc
from dash import html
import pandas as pd
from layouts import Layouts
from data import Data
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



app.layout = Layouts.base(Layouts.market())


if __name__ == '__main__':
    app.run_server(debug=True)