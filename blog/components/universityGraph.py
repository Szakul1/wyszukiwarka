import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from django_plotly_dash import DjangoDash


def create_graphs_universities(university):
    """Tworzy wykres ze statystykami dla uniwersytetu"""
    app = DjangoDash('UniversityGraphs')
    plot_div = {
        'data': [
            {'x': [university.id], 'y': [university.id], 'type': 'bar',
             'name': 'cos'},
        ],
        'layout': {
            'title': 'tescik',
            'xaxis': {
                'title': 'id'
            },
            'yaxis': {
                'title': 'semestr'
            }
        }
    }
    graphs = dbc.Row([
        dcc.Graph(figure=plot_div)
    ])
    app.layout = html.Div(graphs)
