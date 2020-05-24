import dash_core_components as dcc
import dash_html_components as html
from blog.models import Course

from django_plotly_dash import DjangoDash


def create_graph(object_):
    app = DjangoDash('SimpleExample')
    plot_div = {
        'data': [
            {'x': [object_.id], 'y': [object_.semesters], 'type': 'bar',
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
    app.layout = html.Div(dcc.Graph(figure=plot_div))

# figure = go.Figure(go.Indicator(
#     title='cos',
#     mode='gauge+number+delta',
#     delta={'reference': 100},
#     value=10,
#     number={'suffix': "%"},
#     gauge={'shape': 'bullet',
#            'bar': {'thickness': 1},
#            'axis': {'range': [0, 100]}}
# ))
