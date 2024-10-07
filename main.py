from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import countries_df
from builders import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.2/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans:ital@0;1&display=swap"
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        'minHeight': '100vh',
        'backgroundColor': '#111111',
        'color': 'white',
        'fontFamily': 'Open Sans, sans-serif'
    },
    children=[
        html.Header(
            style={'textAlign': 'center', 'paddingTop': '50px'},
            children=[html.H1("Corona Dashboard", style={'fontSize': '40px'})]
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        make_table(countries_df)
                    ]
                )
            ]
        )

    ],
)

if __name__ == '__main__':
    app.run(debug=True)
