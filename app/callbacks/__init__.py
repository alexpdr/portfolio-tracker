from main import app
from dash.dependencies import Input, Output, State
from data import Data
import dash

# TODO: hook to symbols
ids = [f"dropdown-item-{key}" for key in Data.Binance.symbols]

inputs = [
    Input(component_id=f"dropdown-item-{_id}", component_property='n_clicks')
    for _id in ids
]
print(inputs)
@app.callback(
    output=Output(component_id='debugger', component_property='children'),
    inputs=inputs
)
def dropdown_trigger(n_clicks, children):
    print(n_clicks, children)
    return f"{n_clicks}{children}"
