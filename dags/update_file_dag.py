from airflow import DAG, Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'bibiacoutinho'
}

target_file = Dataset("/opt/airflow/output/some_directory/some_file.txt")


def update_file():
    with open(target_file.uri, "w") as f:
        f.write("file updated. ")


with DAG('update_file_dag', start_date=datetime(2023, 1, 1),
         schedule_interval='@daily', catchup=False, default_args=default_args, description='DAG triggers by updating a file (aka dataset).') as dag:

    update_file = PythonOperator(
        task_id='update_file',
        python_callable=update_file,
        outlets=[target_file]
    )
