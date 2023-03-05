from airflow import DAG, Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'bibiacoutinho'
}

target_file = Dataset("/opt/airflow/output/some_directory/some_file.txt")


def update_file():
    with open(target_file.uri, "a") as f:
        f.write("consumer dag was triggered.")


with DAG('consumer_dag', start_date=datetime(2023, 1, 1),
         # schedule to [target_file] means that this DAG will execute when the file is updated by update_file_dag
         schedule=[target_file], catchup=False, default_args=default_args, description='DAG triggers by updating a file (aka dataset).') as dag:

    update_file = PythonOperator(
        task_id='update_file',
        python_callable=update_file
    )
