from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# runs every 10 min
dag = DAG(
    'delete_small_images',
    description='Run scripts to images out of size range DAG',
    start_date=datetime(2023, 3, 22),
    schedule_interval='*/10 * * * *',
    catchup=False
)

delete_small_images_task = BashOperator(
    task_id='delete_small_images_task',
    bash_command='~/codebase/ImageDatasetBuilder/scripts/bash/delete_small_images.sh ',
    dag=dag
)

delete_small_images_task