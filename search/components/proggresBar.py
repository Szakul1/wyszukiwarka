# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
from dash.dependencies import Input, Output


def create(name, value, app, salary=False):
    """Tworzy dany pasek postepu"""
    if salary:  # jesli salary to skaluje z 10k i zamieniam na procenty
        value = salary / 100
        print(value, salary)
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
        if salary:
            return n, f'{salary} zl'
        return n, f"{n} %"

    return progress


def create_progress(course):
    """Tworzy paski postepu w ustawieniu 2x2"""
    app = DjangoDash("Progress", add_bootstrap_links=True)
    row = html.Div([
        dbc.Row([
            dbc.Col(
                create('Wspolczynnik mezczyzn do kobiet', course.m_to_w_ratio,
                       app)),
            dbc.Col(
                create('Wpolczynnik obcokrajowosci', course.international_ratio,
                       app))
        ]),
        dbc.Row([
            dbc.Col(create('Odsetek osob ktore wybraly by ponownie',
                           course.would_choose_again, app)),
            dbc.Col(create('Srednia placa po studiach', course.avg_salary, app,
                           course.avg_salary))
        ]),
    ], style={'width': '98%'})
    app.layout = row
