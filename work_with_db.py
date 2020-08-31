import psycopg2
import os
from os.path import join
import json
from contextlib import closing

conn_params = {
    'dbname': 'plant_pathology',
    'user': 'postgres',
    'password': 'postgres',
    'host': '172.16.0.11',
    'port': '5432'
}


def load_models():
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM models')
            return cursor.fetchall()


def load_config(id):
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT value from config WHERE id = %s', (id,))
            return cursor.fetchall()


def load_history(id):
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT value from history WHERE id = %s', (id,))
            return cursor.fetchall()


def load_cm(id):
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT value from confusion_matrix WHERE id = %s', (id,))
            return cursor.fetchall()


def load_report(id):
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT value from report WHERE id = %s', (id,))
            return cursor.fetchall()
