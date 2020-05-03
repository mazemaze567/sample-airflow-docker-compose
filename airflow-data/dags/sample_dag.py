from datetime import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


with DAG(
        dag_id='sample-dag',
        start_date=datetime(2020, 4, 22),
        schedule_interval=None) as dag:

    def func1():
        logging.info('Hi!')

    task_1 = PythonOperator(
        task_id='task-1',
        python_callable=func1
    )

    task_2 = PythonOperator(
        task_id='task-2',
        python_callable=func1
    )

    task_1 >> task_2
