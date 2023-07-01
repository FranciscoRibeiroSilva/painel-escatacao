from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# import from folders
from app import *
from components import sidebar, dashboard, temp, energia, fumaca, umidade

# DataFrames and Dcc.Store

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),

        dbc.Col([
            html.Div(id="page-content")
        ], md=10),
    ])

#], fluid=True, style={"padding": "0px"}, className="dbc")
], fluid=True)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboard":
        return dashboard.layout

    if pathname == "/temperatura":
        return temp.layout
    
    if pathname == "/energia":
        return energia.layout

    if pathname == "/fumaca":
        return fumaca.layout
    
    if pathname == "/umidade":
        return umidade.layout

if __name__ == '__main__':
    app.run_server(debug=True)