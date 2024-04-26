from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define the DAG
dag = DAG(
    'delete_n_images',
    description='Run scripts to remove bad images DAG',
    start_date=datetime(2023, 3, 22),
    schedule_interval='*/20 * * * *',
    catchup=False
)


delete_n_images_task = BashOperator(
    task_id='delete_n_images_task',
    bash_command='/home/priyan/codebase/DatasetBuilder/datasetbuilder-python/src/main/scripts/bash/delete_n_images.sh ',
    dag=dag
)

# Define the task dependencies
delete_n_images_task