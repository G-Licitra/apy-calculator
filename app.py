# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from scr.logic import asset_over_time_apy

app = Dash(__name__)


app.layout = html.Div([
    html.Div(children=[
        html.H1('Annual Interest Yiled Calculator'),
        
        html.Br(),
        html.Label('Initial Investment P'),
        dcc.Input(id='initial-investment', value=1000, type="number"),
        
        html.Br(),
        html.Label('Annual Interest Rate [r]'),
        dcc.Input(id='annual-interest-rate', value=.05, type="number"),
        
        html.Br(),
        html.Label('Number of compounding periods per year [n]'),
        dcc.Input(id= 'compounding-periods-per-year', value=12, type="number"),
        
        html.Br(),
        html.Label('Number of years [t]'),
        dcc.Input(id='number-of-years', value=10, type="number"),
        
        dcc.Graph(id='asset-apy-over-time'),
    
    ], style={'padding': 10, 'flex': 1}),

], style={'display': 'flex', 'flex-direction': 'row'})


@app.callback(
    Output(component_id='asset-apy-over-time', component_property='figure'),
    Input(component_id='initial-investment', component_property='value'),
    Input(component_id='annual-interest-rate', component_property='value'),
    Input(component_id='compounding-periods-per-year', component_property='value'),
    Input(component_id='number-of-years', component_property='value'),
)
def update_figure(P,r,n,t):
    df = asset_over_time_apy(P=P, r=r, n=n, t=t)
    
    fig = px.scatter(data_frame=df, x="time", y="value",  size_max=55)

    fig.update_layout(transition_duration=500)
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)