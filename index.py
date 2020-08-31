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
from apps import model, learning_history
import work_with_db as db



'''
Это типо прототип , но уже вроде нот бед
короче идея вынести всю работу с бд в отдельный питон файл
work_with_db.py
там написать функции подгрузки моделей
подгрузки config,report,cm,history по id

'''

# models = db.load_models()
# config = db.load_config(20)
# report = db.load_report(20)
# cm = db.load_cm(20)
# history = db.load_history(20)

models = [
    (0, "Test Dummy Model #1", "EFN"),
    (1, "Test Dummy Model #2", "EFN"),
]

reports = [
    (0, {
        "accuracy": "0.1979166716337204",
        "val_accuracy": "0.0",
        "loss": "3.4406051635742188",
        "val_loss": "4.19291353225708",
        "f1": "0.0",
        "val_f1": "0.0",
        "test_accuracy": "0.0",
        "test_loss": "4.24012565612793",
        "test_f1": "0.0"
    }),
    (0, {
        "accuracy": "0.1979166716337204",
        "val_accuracy": "0.0",
        "loss": "3.4406051635742188",
        "val_loss": "4.19291353225708",
        "f1": "0.0",
        "val_f1": "0.0",
        "test_accuracy": "0.0",
        "test_loss": "4.24012565612793",
        "test_f1": "0.0"
    })
]

reports = [
    (id, {
        name: float(value)
        for name, value in report.items()
    })
    for id, report in reports
]

histories = [
    (0, {
        "loss": ["3.946352958679199", "3.4406051635742188"],
        "accuracy": ["0.0572916679084301", "0.1979166716337204"],
        "f1": ["0.0", "0.0"],
        "val_loss": ["4.087198734283447", "4.19291353225708"],
        "val_accuracy": ["0.0", "0.0"],
        "val_f1": ["0.0", "0.0"],
        "lr": ["0.001", "0.001"]
    }),
    (1, {
        "loss": ["2.946352958679199", "1.4406051635742188"],
        "accuracy": ["0.0572916679084301", "0.1979166716337204"],
        "f1": ["0.0", "0.0"],
        "val_loss": ["4.087198734283447", "4.19291353225708"],
        "val_accuracy": ["0.0", "0.0"],
        "val_f1": ["0.0", "0.0"],
        "lr": ["0.001", "0.001"]
    }),
]

histories = [
    (id, {
        name: [float(value) for value in values]
        for name, values in history.items()
    })
    for id, history in histories
]

graphs = (
    ("loss", [0, 1.1]),
    ("accuracy", [0, 1.1]),
    ("f1", [-0.1, 3]),
    ("val_loss", [-0.1, 3]),
    ("val_f1", [-0.1, 1.1]),
    ("lr", [-0.1, 1.1])
)


def get_dropdown_list(models):
    return [
        {'label': str(model[1]),
         'value': model[0]} for model in models
    ]


app.layout = html.Div([
    #dcc.Location(id="url", refresh=False),
    dcc.Dropdown(
        id='models-dropdown',
        options=get_dropdown_list(models),
        clearable=True,
        multi=True,
        value=[],
    ),
    html.Div(
        learning_history.generate_layout(graphs),
        id='page-content',
    ),
    html.Div(id='dummy')
])


@app.callback(
    [Output(graph, 'figure') for graph, _ in graphs],
    [Input('models-dropdown', 'value')])
def display_page(value):
    return learning_history.update_figures(
        graphs,
        [h[1] for h in histories if h[0] in value],
        [m[1] for m in models if m[0] in value])


if __name__ == '__main__':
    app.run_server(debug=True)

