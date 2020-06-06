import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash


def create_graph(x, y, title, y_name):
    plot_div = {
        'data': [
            {'x': x,
             'y': y,
             'type': 'bar'},
        ],
        'layout': {
            'title': title,
            'xaxis': {
                'title': 'nazwa'
            },
            'yaxis': {
                'title': y_name
            },
        }
    }
    return plot_div


def create_comparison(objects):
    """Tworzy wkyres porownan dla danych obiektow"""
    app = DjangoDash('Comparison')
    names = [i.name + '(' + i.type_1 + ')' for i in objects]
    app.layout = html.Div([
        dcc.Graph(figure=create_graph(names, [i.m_to_w_ratio for i in objects],
                                      'Wspolczynnik mezczyzn do kobiet',
                                      'Wspolczynnik')),
        dcc.Graph(
            figure=create_graph(names, [i.international_ratio for i in objects],
                                'Wspolczynnik obcokrajowcow',
                                'Wpolczynnik')),
        dcc.Graph(
            figure=create_graph(names, [i.would_choose_again for i in objects],
                                'Odsetek osob, ktore wybraly by ponownie',
                                'Odsetek')),
        dcc.Graph(figure=create_graph(names, [i.avg_salary for i in objects],
                                      'Srednia placa po studiach',
                                      'Placa'))
    ])
