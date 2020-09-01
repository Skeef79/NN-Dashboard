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


def get_db_params():
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


model.update_models(**get_db_params())
app.layout = model.get_layout()

if __name__ == '__main__':
    app.run_server(debug=True)

