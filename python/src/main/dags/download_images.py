from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# runs on demand
dag = DAG(
    'download_images',
    description='Run scripts to remove bad images DAG',
    start_date=datetime(2023, 3, 22),
    catchup=False
)



download_images_task = BashOperator(
    task_id='download_images_task',
    bash_command='~/codebase/ImageDatasetBuilder/scripts/bash/download_images.sh ',
    dag=dag
)



download_images_task