import dash
from dash.dependencies import Input,Output
import dash_core_components as dcc
import dash_html_components as html
import pickle
import plotly.graph_objs as go
import json
import numpy as np
from dash_core_components import Dropdown
from dash_html_components import Div
from app import app
import work_with_db as db

models = []
configs = []
cms = []


def update_models(new_models, new_cms, new_configs):
    global models, configs, cms
    models.clear()
    configs.clear()
    cms.clear()

    models.extend(new_models)
    configs.extend(new_configs)
    cms.extend(new_cms)


def get_confusion_matrix(cm, labels):
    """
    :param cm: [[value]] confusion matrix
    :param labels: labels for confusion matrix
    :return: confusion matrix Div block
    """

    cm_arr = np.array(cm)
    cm_arr = cm_arr.T
    cm_arr = cm_arr.tolist()
    data = go.Heatmap(z=cm_arr, x=labels, y=labels, colorscale="ylgn")  # ylgn #blues #pinkyl
    annotations = []

    for i, row in enumerate(cm):
        for j, value in enumerate(row):
            annotations.append(
                {
                    "x": labels[i],
                    "y": labels[j],
                    "font": {"color": "black"},
                    "text": str(value),
                    "xref": "x1",
                    "yref": "y1",
                    "showarrow": False
                }
            )
    layout = {
        "xaxis": {"title": "Predicted value", "showticklabels": False},
        "yaxis": {"title": "Real value", "showticklabels": False},
        "annotations": annotations,
        "height": 1000
    }
    fig = go.Figure(data=data, layout=layout)
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)

    return html.Div(children=[
        dcc.Graph(id="confusion_matrix",
                  figure=fig,
                  config={
                      'displayModeBar': False,
                      'scrollZoom': False}),
    ])


def get_dropdown_list(models):
    return [
        {'label': str(model[1]),
         'value': model[0]} for model in models
    ]


def get_layout():
    return Div([
        html.H2("Confusion Matrix"),
        Dropdown(
            id='cm-dropdown',
            options=get_dropdown_list(models),
            clearable=True,
            value=-1
        ),
        Div(id='cm-out')
    ])


@app.callback(Output('cm-out', 'children'),
              [Input('cm-dropdown', 'value')])
def display_cm(value):
    cm = [c for i, c in cms if i == value]
    if not cm:
        return ""

    cm = cm[0]
    cfg = [c for i, c in configs if i == value][0]
    cm = [[int(x) for x in sub_cm] for sub_cm in cm]

    return get_confusion_matrix(cm, cfg['classes'])



