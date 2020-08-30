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


def load_models():
    with closing(psycopg2.connect(dbname='plant_pathology',
                                  user='postgres',
                                  password='postgres',
                                  host='172.16.0.11',
                                  port='5432')) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM models')
            return cursor.fetchall()


def get_dropdown_list(models):
    return [
        {'label': str(model[1]),
         'value': str(model[0])} for model in models]


models = load_models()
print(models)


app.layout = html.Div([
    dcc.Dropdown(
        id='models-dropdown',
        options=get_dropdown_list(models),
    ),
    html.Div(id='dd-output-container')
])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('models-dropdown', 'value')])

def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=False)

