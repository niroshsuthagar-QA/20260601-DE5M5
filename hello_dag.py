
from datetime import datetime, timedelta
 
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
 
 
# ------------------------------------------------------------------------------
# Default arguments applied to every task in the DAG unless overridden.
# ------------------------------------------------------------------------------
default_args = {
    "owner": "demo",
    "retries": 1,                       # retry a failed task once
    "retry_delay": timedelta(minutes=1) # wait 1 min between retries
}
 
 
# ------------------------------------------------------------------------------
# Python callables used by the PythonOperators below.
# ------------------------------------------------------------------------------
def push_message(**context):
    """Push a message into XCom so a downstream task can read it."""
    message = f"Hello from Airflow at {datetime.utcnow().isoformat()}"
    print(f"[push] Pushing message to XCom: {message}")
    # Returning a value automatically pushes it to XCom under key 'return_value'.
    return message
 
 
def pull_message(**context):
    """Pull the message that push_message stored in XCom and print it."""
    ti = context["ti"]  # 'ti' = TaskInstance, the handle for XCom access.
    message = ti.xcom_pull(task_ids="push_message_task")
    print(f"[pull] Received message from XCom: {message}")
 
 
# ------------------------------------------------------------------------------
# DAG definition. The 'with DAG(...)' context manager auto-registers tasks.
# ------------------------------------------------------------------------------
with DAG(
    dag_id="hello_airflow",
    description="A simple scheduled demo DAG",
    default_args=default_args,
    # start_date in the past so the scheduler can begin immediately.
    start_date=datetime(2024, 1, 1),
    # Run every 5 minutes. Accepts cron strings or presets like '@daily'.
    schedule="*/5 * * * *",
    # Don't backfill all missed runs since start_date - only run going forward.
    catchup=False,
    # Tags show up in the UI for easy filtering.
    tags=["demo", "tutorial"],
) as dag:
 
    # Task 1: a simple shell command.
    task_1 = BashOperator(
        task_id="print_date_task",
        bash_command="echo 'Pipeline started at:' && date",
    )
 
    # Task 2: run our push_message Python function.
    task_2 = PythonOperator(
        task_id="push_message_task",
        python_callable=push_message,
    )
 
    # Task 3: run our pull_message Python function.
    task_3 = PythonOperator(
        task_id="pull_message_task",
        python_callable=pull_message,
    )
 
    # Define execution order: task_1 -> task_2 -> task_3
    task_1 >> task_2 >> task_3
 
