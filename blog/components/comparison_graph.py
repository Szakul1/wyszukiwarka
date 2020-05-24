import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash


def create_comparison(objects):
    app = DjangoDash('Comparison')
    print(objects)
    plot_div = {
        'data': [
            {'x': [i.name for i in objects],
             'y': [i.semesters for i in objects],
             'type': 'bar'},
        ],
        'layout': {
            'title': 'porownanie',
            'xaxis': {
                'title': 'nazwa'
            },
            'yaxis': {
                'title': 'semestr'
            }
        }
    }
    app.layout = html.Div(dcc.Graph(figure=plot_div))
