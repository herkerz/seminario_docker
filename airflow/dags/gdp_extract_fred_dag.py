
from datetime import datetime
import numpy as np
import pandas as pd
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.sqlite_operator import SqliteOperator
from sql_commands import SQL_CREATE
from functions import _get_series_data, _insert_data


default_args = {'owner': 'seminario_itba', 'retries': 0, 'start_date': datetime(2023, 10, 1)}
with DAG('gdp_data', default_args=default_args, schedule_interval='0 23 1 * *') as dag:
    create_table_if_not_exists = SqliteOperator(
        task_id='create_table_if_not_exists',
        sql=SQL_CREATE,
        sqlite_conn_id='sqlite_default',
    )
    get_gdp_data = PythonOperator(
        task_id='get_gdp_data',
        python_callable=_get_series_data,
        op_args=['gdp'],
    )
    # Add insert gdp data
    insert_gdp_data = PythonOperator(
        task_id='insert_gdp_data',
        python_callable=_insert_data,

    )
    create_table_if_not_exists >> get_gdp_data >> insert_gdp_data