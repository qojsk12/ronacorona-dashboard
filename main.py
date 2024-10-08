from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import countries_df
from data import totals_df
from builders import make_table
from dash.dependencies import Input, Output


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.2/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans:ital@0;1&display=swap"
]

app = Dash(__name__, external_stylesheets=stylesheets)


bubble_map = px.scatter_geo(
    countries_df,
    size="Confirmed",
    hover_name="Country_Region",
    color="Confirmed",
    color_continuous_scale=px.colors.sequential.Oryel,
    locations="Country_Region",
    locationmode="country names",
    size_max=40,
    title="Confirmed By Country",
    template="plotly_dark",
    hover_data={
        "Confirmed": ":,2f",
        "Deaths": ":,2f",
        "Recovered": ":,2f",
        "Country_Region": False
    })
bubble_map.update_layout(
    margin=dict(l=0, r=0, t=50, b=0)
)

bars_graph = px.bar(
    totals_df,
    x='condition',
    y='count',
    template="plotly_dark",
    title="Total Global Cases",
    labels={
        "condition": "Condition",
        "count": "Count",
        "color": "Condition"
    },
    hover_data={
        'count': ':,'
    }
)

bars_graph.update_traces(
    marker_color=["#e74c3c", "#8e44ad", "#27ae60"]
)

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
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)"
            },
            children=[
                html.Div(
                    style={
                        "grid-column": "span 3",
                    },
                    children=[
                        dcc.Graph(figure=bubble_map)
                    ]
                ),
                html.Div(
                    children=[
                        make_table(countries_df)
                    ]
                )
            ]
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)"
            },
            children=[
                html.Div(
                    children=[
                        dcc.Graph(figure=bars_graph)
                    ]
                ),
                html.Div(
                    children=[
                        dcc.Input(placeholder="what is your name?",
                                  id="hello-input"),
                        html.H2(children="Hello anonymous", id="hello-output")
                    ]
                )
            ]
        )
    ],
)


@app.callback(
    Output("hello-output", "children"),
    [
        Input("hello-input", "value")
    ]
)
def update_hello(value):
    if value is None:
        return "Hello Anonymous"
    else:
        return f"Hello {value}"


if __name__ == '__main__':
    app.run(debug=True)
