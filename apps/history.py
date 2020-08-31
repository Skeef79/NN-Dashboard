from dash_core_components import Graph
from dash_html_components import Div, H1

layout = Div(children = [
    H1(children="История обучения"),
    # generate_table(metrics_table.report),
    Div(className="metrics_bottom_border"),
    Div(
        children=Div(
            Graph(

            )
        ),
        className='history_graphs'),

    Div(id="history_graphs-display-value"),
])