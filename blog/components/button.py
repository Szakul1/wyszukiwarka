import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash
from django.shortcuts import redirect
from dash.dependencies import Input, Output, State
from .comparison_graph import create_comparison

created = False


def is_created():
    if created:
        return
    else:
        app = DjangoDash('Comparison')
        app.layout = html.Div()


def create_checkbox(objects):
    objects_id = [i.id for i in objects]

    app = DjangoDash('Button', add_bootstrap_links=True)

    app.layout = html.Div([
        dbc.Button("Compare", id='button', color='primary', size="lg",
                   className="mr-1"),
        html.Div(id='hidden')
    ])

    @app.callback(
        Output('hidden', 'children'),
        [
            Input('button', 'n_clicks'),
        ]
    )
    def on_button_click(n):
        global created
        if n:
            print(checked_id)
            created = True
            create_comparison([i for i in objects if str(i.id) in checked_id])
            # redirect('universities/')
            # return dcc.Location(pathname='', id='adns')

    checked_id = []
    called = [False for _ in range(len(objects_id) + 1)]
    for i in range(1, len(objects_id) + 1):
        app = DjangoDash('Check' + str(i), add_bootstrap_links=True)
        checkbox = dbc.Checklist(
            options=[
                {'value': 1},
            ],
            id=str(i)
        )
        app.layout = html.Div([
            checkbox,
            html.Div(id='hidden'),
            dcc.Interval('Interval' + str(i), )
        ])

        @app.callback(
            Output('hidden', 'children'),
            [
                Input(str(i), 'id'),
                Input(str(i), 'value')
            ],
        )
        def on_check(n, value):
            if called[int(n)]:
                called[int(n)] = False
                return
            if value:
                checked_id.append(n)
            elif n in checked_id:
                checked_id.remove(n)

        @app.callback(
            Output(str(i), 'value'),
            [
                Input('Interval' + str(i), 'n_intervals'),
                Input('Interval' + str(i), 'id')
            ]
        )
        def update(n, interval_id):
            interval_id = interval_id.strip('Interval')
            called[int(interval_id)] = True
            if interval_id in checked_id:
                return [1]
            else:
                return []

    app = DjangoDash('Checkall', add_bootstrap_links=True)
    app.layout = html.Div([
        dbc.Checklist(
            options=[
                {'label': 'Zaznaczy wszystkie', 'value': 1}
            ], id='checkall'
        ),
        html.Div(id='hidden')
    ])

    @app.callback(
        Output('hidden', 'children'),
        [
            Input('checkall', 'value')
        ],
    )
    def check_all(value):
        nonlocal checked_id
        if value:
            checked_id = [str(i) for i in objects_id]
        else:
            checked_id = []