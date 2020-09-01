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
from apps import model, learning_history, report_table
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

app.layout = model.layout


if __name__ == '__main__':
    app.run_server(debug=True)

