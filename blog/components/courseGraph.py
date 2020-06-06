import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

from django_plotly_dash import DjangoDash


def create_graph(course):
    """Tworzy wykres z iloscia miejsc od czasu dla uniwersytetu
    Dane na podstawie wartosci course.function
    """
    app = DjangoDash('CourseGraph')
    plot_div = {
        'data': [
            {'x': list(range(2011, 2021)),
             'y': [course.function * i for i in np.arange(1, 2, 0.1)],
             'type': 'bar',
             'name': 'cos'},
        ],
        'layout': {
            'title': 'Liczba miejsc w czasie',
            'xaxis': {
                'title': 'Lata'
            },
            'yaxis': {
                'title': 'Liczba miejsc'
            }
        }
    }
    graph = dcc.Graph(figure=plot_div)
    app.layout = html.Div(graph)
