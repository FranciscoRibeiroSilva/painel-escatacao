import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from datetime import date, datetime, timedelta

import pdb
from dash_bootstrap_templates import ThemeChangerAIO

# ========= DataFrames ========= #
import numpy as np
import pandas as pd
#from globals import *

card_icon ={
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}


# ========= Layout ========= #
layout = dbc.Col([
                dbc.Row([
                    #temperatura
                    dbc.Col([
                        dbc.CardGroup([
                            dbc.Card([
                                html.Legend('Temperatura'),
                                html.H5('334 c', id='p-temperatura-dashboards', style={})
                            ], style={'padding-left':'20px', 'padding-top':'10px'}),
                            dbc.Card(
                                html.Div(className='fa fa-temperature', style=card_icon),
                                color='warning',
                                style={'maxWidth': 75, 'heigth': 100, 'margin-left': '-10px'}
                            )
                        ])
                    ], width=4),
                    #umidade
                    dbc.Col([
                        dbc.CardGroup([
                            dbc.Card([
                                html.Legend('umidade'),
                                html.H5('334 c', id='p-umidade-dashboards', style={})
                            ], style={'padding-left':'20px', 'padding-top':'10px'}),
                            dbc.Card(
                                html.Div(className='fa-solid fa-hand-holding-droplet', style=card_icon),
                                color='blue',
                                style={'maxWidth': 75, 'heigth': 100, 'margin-left': '-10px'}
                            )
                        ])
                    ], width=4),
                    
                    #fumaça
                    dbc.Col([
                        dbc.CardGroup([
                            dbc.Card([
                                html.Legend('CO²'),
                                html.H5('334 c', id='p-CO²-dashboards', style={})
                            ], style={'padding-left':'20px', 'padding-top':'10px'}),
                            dbc.Card(
                                html.Div(className='fa-brands fa-free-code-camp', style=card_icon),
                                #<i class="fa fa-university"></i>
                                color='danger',
                                style={'maxWidth': 75, 'heigth': 100, 'margin-left': '-10px'}
                            )
                        ])
                    ], width=4)
                ], style={'margin': '10px'}),

                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            html.Legend("Filtro", className="card-title"),
                            html.Label("Categoria"),
                            html.Div(
                                dcc.Dropdown(
                                id='"dropdown-tem',
                                clearable=False,
                                style={'width': "100%"},
                                persistence=True,
                                persistence_type="session",
                                multi=True)
                            ),

                            html.Label("Categoria das", style={"margin-top": "10px"}),
                            dcc.Dropdown(
                                id="dropdown-des",
                                clearable=False,
                                style={"width": "100%"},
                                persistence=True,
                                persistence_type="session",
                                multi=True
                            ),

                            html.Legend("periodo de analise", style={"margin-top": "10px"}),
                            dcc.DatePickerRange(
                                month_format= 'Do MMM YYY',
                                end_date_placeholder_text='Data...',
                                start_date=datetime.today(),
                                end_date=datetime.today() + timedelta(days=31),
                                updatemode='singledate',
                                style={'z-index': '100'})],
                                
                                style={"height": "100%", "padding": "20px"}),
                    ], width=4),
                    dbc.Col(
                        dbc.Card(dcc.Graph(id='graph1'), style={'height': '100%', 'padding': '10px'}), width=8
                    )
                ], style={'margin':'10px'}),

                dbc.Row([
                    dbc.Col(dbc.Card(dcc.Graph(id='graph2'), style={'padding': '10px'}), width=6),
                    dbc.Col(dbc.Card(dcc.Graph(id='graph3'), style={'padding': '10px'}), width=3),
                    dbc.Col(dbc.Card(dcc.Graph(id='graph4'), style={'padding': '10px'}), width=3),
                ], style={"margin": "10px"})
            ])





# =========  Callbacks  =========== #
# Pop-up receita

# ========= Layout ========= #
#layout = dbc.Col([
#    html.H1('Zôi', className='text-primary'),
#    html.P('Uespi', className='text-info'),
#    html.Hr(),
#
#    #_____logo_________#
#    dbc.Button(id='botton_avatar', children=[html.Img(src='/assent/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_name')])
#
#
#            ])
#
# =========  Callbacks  =========== #
# Pop-up receita
