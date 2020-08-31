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


'''
Это типо прототип , но уже вроде нот бед
короче идея вынести всю работу с бд в отдельный питон файл
work_with_db.py
там написать функции подгрузки моделей
подгрузки config,report,cm,history по id

'''


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
    #dcc.Location(id="url", refresh=False),
    dcc.Dropdown(
        id='models-dropdown',
        options=get_dropdown_list(models),
        clearable=False,
        value=models[0][0]
    ),
    html.Div(id='page-content')
])


@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [Input('models-dropdown', 'value')])
def display_page(value):
    return index2.gen_layout(value)


if __name__ == '__main__':
    app.run_server(debug=True)

