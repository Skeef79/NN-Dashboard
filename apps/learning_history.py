from dash_core_components import Graph
from dash_html_components import Div, H1, H2
from plotly.graph_objs import Figure, Scatter


def generate_layout(graphs):
    return Div([
        H1("История обучения"),
        Div(className="metrics_bottom_border"),
        Div(
            children=[Div([
                Graph(
                    id=name,
                )
            ]) for name, _ in graphs],
            className='history_graphs'),
    ])


def update_figures(graphs, histories, models):
    """Returns new figures for current dropdown state;
    graphs is [(graph_name, graph_range)],
    histories is [{graph_name: [values]}],
    models is [(id, name, type)]"""
    return [
        Figure(
            data=[
                Scatter(
                    x=[x for x in range(len(history['loss']))],
                    y=history[name],
                    name=model,
                )
                for history, model in zip(histories, models)
            ],
            layout=dict(
                showlegend=True,
                title={
                    "text": name,
                    "x": 0.5,
                    "font": dict(
                        family="Courier New, monospace",
                        size=40),
                    "xanchor": 'center',
                    "yanchor": "top"
                },
                xaxis_title='Epoch',
                yaxis_title=name,
                yaxis_range=range_,
                font=dict(
                    family="Courier New, monospace",
                    size=18
                ),
            )
        )
        for name, range_ in graphs
    ]
