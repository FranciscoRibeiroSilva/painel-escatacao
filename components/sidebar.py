import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from datetime import datetime, date

import pdb
from dash_bootstrap_templates import ThemeChangerAIO

#dataframe
import numpy as np
import pandas as pd
from globals import *

#layout
layout = dbc.Card([
    html.H1("Painel", className="text-primary"),
    html.P("da estação", className="text-info"),
    html.Hr(),

    #perfil
    dbc.Button(id='botão_avatar',
        children=[html.Img(src="assets/img_fem.png", id="avatar_change", className='perfil_avatar'),
    ], style={'backgorud-color': 'transparent', 'border-color': 'transparent'}),

        
# Seção NAV ----------------------

    html.Hr(),
    dbc.Nav(
        [
            dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
            dbc.NavLink("Temperatura", href="/temperatura", active="exact"),
            dbc.NavLink("Umidade", href="/umidade", active="exact"),
            dbc.NavLink("Energia", href="/energia", active="exact"),
            dbc.NavLink("Fumaça", href="/fumaca", active="exact"),
        ], vertical=True, pills=True, id="nav_buttons", style={"margin-bottom":"50px"}
    ),


    
        ], id='sidebar_completa'
    )




# =========  Callbacks  =========== #
# Pop-up receita
