import dash_html_components as html
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
from dash.dependencies import Input, Output


def create(name, value, app):
    """Tworzy dany pasek postepu"""
    progress = html.Div(
        [
            dbc.Label(name),
            dcc.Interval(id=name + "-interval", n_intervals=0, interval=10,
                         max_intervals=value),
            dbc.Progress(id=name,
                         style={"height": "30px"},
                         className='mb-3', striped=True),
        ]
    )

    @app.callback(
        [Output(name, "value"), Output(name, "children")],
        [Input(name + "-interval", "n_intervals")],
    )
    def update_progress(n):
        """Uaktualnia pasek postepu tworzac animacje ladowania"""
        return n, f"{n} %"

    return progress


def create_progress():
    """Tworzy paski postepu w ustawieniu 2x2"""
    app = DjangoDash("Progress", add_bootstrap_links=True)
    row = html.Div([
        dbc.Row([
            dbc.Col(create('first', 10, app)),
            dbc.Col(create('second', 20, app))
        ]),
        dbc.Row([
            dbc.Col(create('third', 30, app)),
            dbc.Col(create('fourth', 40, app))
        ]),
    ], style={'width': '98%'})
    app.layout = row
