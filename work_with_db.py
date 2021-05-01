import psycopg2
import os
from os.path import join
import json
from contextlib import closing

conn_params = {
    'dbname': 'example',
    'user': 'Igor',
    'password': 'pass',
    'host': '1.2.3.4',
    'port': '1234'
}


def load_models():
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM models')
            return cursor.fetchall()


def load_configs():
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM config')
            return cursor.fetchall()


def load_histories():
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM history')
            return cursor.fetchall()


def load_cms():
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM confusion_matrix')
            return cursor.fetchall()


def load_reports():
    with closing(psycopg2.connect(**conn_params)) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM report')
            return cursor.fetchall()
