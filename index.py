import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import psycopg2
import os
from os.path import join
from contextlib import closing
import json
from app import app
import dash
from apps import model, confusion_matrix
import work_with_db as db


def get_learning_params():
    return {
        'new_models': db.load_models(),
        'new_reports': [
                (id, {
                    name: float(value)
                    for name, value in report.items()
                })
                for id, report in db.load_reports()
            ],
        'new_histories': [
                (id, {
                    name: [float(value) for value in values]
                    for name, values in history.items()
                })
                for id, history in db.load_histories()]
    }


def get_cm_params():
    return {
        'new_models': db.load_models(),
        'new_cms': db.load_cms(),
        'new_configs': db.load_configs()
    }


model.update_models(**get_learning_params())
confusion_matrix.update_models(**get_cm_params())

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(
        [
            dcc.Link(
                "История обучения",
                href="/apps/model",
                className="tab first",
            ),
            dcc.Link(
                "Confusion matrix",
                href="/apps/confusion_matrix",
                className="tab"
            ),
        ],
        className="links",
    ),
    html.Div(id="page-content"),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == 'apps/model':
        model.update_models(**get_learning_params())
        return model.get_layout()
    elif pathname == '/apps/confusion_matrix':
        confusion_matrix.update_models(**get_cm_params())
        return confusion_matrix.get_layout()
    else:
        model.update_models(**get_learning_params())
        return model.get_layout()


if __name__ == '__main__':
    app.run_server(debug=True)

