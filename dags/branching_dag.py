from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator


def _run_this_first(ti):
    print("run_this_first")
    ti.xcom_push(key="my_key", value="a")


def _branch(ti):
    print("branch")
    value = ti.xcom_pull(key="my_key", task_ids="run_this_first")
    if (value == 'a'):
        return 'branch_a'
    return "branch_b"


def _branch_a():
    print("branch_a")


def _branch_b():
    print("branch_b")


def _after_branch_a():
    print("after_branch_a")


with DAG("branch_dag", start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:

    run_this_first = PythonOperator(
        task_id='run_this_first',
        python_callable=_run_this_first
    )

    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=_branch
    )

    branch_a = PythonOperator(
        task_id='branch_a',
        python_callable=_branch_a
    )

    branch_b = PythonOperator(
        task_id='branch_b',
        python_callable=_branch_b
    )

    after_branch_a = PythonOperator(
        task_id='after_branch_a',
        python_callable=_after_branch_a
    )

    run_this_first >> branch >> [branch_a, branch_b]

    branch_a >> after_branch_a
