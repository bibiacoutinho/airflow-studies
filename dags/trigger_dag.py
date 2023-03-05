import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

default_args = {
    'owner': 'bibiacoutinho'
}


def create_directory_file(path):
    directory = os.path.join(path, 'some_directory')
    cmd = 'mkdir ' + directory
    os.system(cmd)
    cmd = 'chmod -R 777 ' + directory
    os.system(cmd)
    cmd = 'cd ' + directory
    cmd = 'touch '+directory+'/some_file.txt'
    os.system(cmd)
    cmd = 'chmod -R 777 ' + directory+'/some_file.txt'
    os.system(cmd)


with DAG('trigger_dag', start_date=datetime(2023, 1, 1),
         schedule_interval='@daily', catchup=False, default_args=default_args, description='DAG triggers target_dag.') as dag:

    create_directory_file = PythonOperator(
        task_id='create_directory_file',
        python_callable=create_directory_file,
        op_kwargs={'path': '/opt/airflow/output/'}
    )

    trigger_target_dag = TriggerDagRunOperator(
        task_id="trigger_target_dag",
        trigger_dag_id="target_dag"
    )

create_directory_file >> trigger_target_dag