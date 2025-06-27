import sys
import os

# Adiciona a pasta scripts ao PYTHONPATH para que os imports funcionem no Airflow
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from scripts.extract import fetch_breweries
from scripts.transform import transform_data
from scripts.aggregate import aggregate_data

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False
}

default_start_date = datetime(2023, 1, 1)

dag = DAG(
    'brewery_etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL para cervejarias',
    schedule_interval='@daily',
    start_date=default_start_date,
    catchup=False
)

with dag:
    extract_task = PythonOperator(
        task_id='extract_breweries',
        python_callable=fetch_breweries
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    aggregate_task = PythonOperator(
        task_id='aggregate_data',
        python_callable=aggregate_data
    )

    extract_task >> transform_task >> aggregate_task
