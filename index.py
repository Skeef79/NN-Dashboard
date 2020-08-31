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
from apps import model, history
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

report = {
    "accuracy": "0.1979166716337204",
    "val_accuracy": "0.0",
    "loss": "3.4406051635742188",
    "val_loss": "4.19291353225708",
    "f1": "0.0",
    "val_f1": "0.0",
    "test_accuracy": "0.0",
    "test_loss": "4.24012565612793",
    "test_f1": "0.0"
}




def get_dropdown_list(models):
    return [
        {'label': str(model[1]),
         'value': str(model[0])} for model in models
    ]


# app.layout = html.Div([
#     #dcc.Location(id="url", refresh=False),
#     dcc.Dropdown(
#         id='models-dropdown',
#         options=get_dropdown_list(models),
#         clearable=False,
#         value=models[0][0]
#     ),
#     html.Div(id='page-content')
# ])
#
#
# @app.callback(
#     dash.dependencies.Output('page-content', 'children'),
#     [Input('models-dropdown', 'value')])
# def display_page(value):
#     return model.gen_layout(value)

app.layout = history.layout


if __name__ == '__main__':
    app.run_server(debug=True)

