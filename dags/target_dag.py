import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'bibiacoutinho'
}


def create_other_file(path):
    f = open(path+"other_file.txt", "x")
    f.write("Hello, file!")
    f.close()
    cmd = 'chmod -R 777 ' + path + "other_file.txt"
    os.system(cmd)


with DAG('target_dag', start_date=datetime(2023, 1, 1),
         schedule_interval=None, catchup=False, default_args=default_args, description='DAG is executed after trigger_dag finishes with success.') as dag:

    create_other_file = PythonOperator(
        task_id='create_other_file',
        python_callable=create_other_file,
        op_kwargs={'path': '/opt/airflow/output/some_directory/'}
    )

create_other_file
