import dash_bootstrap_components as dbc
import dash_html_components as html
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output
from .comparison_graph import create_comparison

created = False


def is_created():
    """Jesli Comparison nie jest stworzony to tworzy pusta aplikacje"""
    if created:
        return
    else:
        app = DjangoDash('Comparison')
        app.layout = html.Div()


def create_checkbox(objects):
    """Przyjmuje obiekty. Dla kazdego tworzy checkboxa. Tworzy guzik porownaj
    oraz zaznacz wszystkie.
    """
    objects_id = [i.id for i in objects]
    print(objects_id)

    app = DjangoDash('Button', add_bootstrap_links=True)

    app.layout = html.Div([
        dbc.Button("Porownaj", id='button', color='primary', size="sg",
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
        """Podczas klikniecia tworzy wykres do porownan miedzy obiektami"""
        global created
        if n:
            created = True
            create_comparison([i for i in objects if str(i.id) in checked_id])

    checked_id = []
    for i in objects_id:
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
        ])

        @app.callback(
            Output('hidden', 'children'),
            [
                Input(str(i), 'id'),
                Input(str(i), 'value')
            ],
        )
        def on_check(n, value):
            """Na zaznaczeniu usuwa lub dodaje do list check_id id obiektu"""
            if value:
                checked_id.append(n)
            elif n in checked_id:
                checked_id.remove(n)
