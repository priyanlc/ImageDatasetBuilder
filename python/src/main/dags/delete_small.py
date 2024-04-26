from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define the DAG
dag = DAG(
    'clean_images',
    description='Run scripts to remove bad images DAG',
    start_date=datetime(2023, 3, 22),
    schedule_interval='*/10 * * * *',
    catchup=False
)

# Define the BashOperator task
delete_small_images_task = BashOperator(
    task_id='delete_small_images_task',
    bash_command='/home/priyan/codebase/DatasetBuilder/datasetbuilder-python/src/main/scripts/bash/delete_small_images.sh ',
    dag=dag
)

# Define the BashOperator task
delete_no_face_images_task = BashOperator(
    task_id='delete_no_face_images_task',
    bash_command='/home/priyan/codebase/DatasetBuilder/datasetbuilder-python/src/main/scripts/bash/deep_face.sh ',
    dag=dag
)


face_recognition_task = BashOperator(
    task_id='face_recognition_task',
    bash_command='/home/priyan/codebase/DatasetBuilder/datasetbuilder-python/src/main/scripts/bash/face_recognition.sh ',
    dag=dag
)

delete_n_images_task = BashOperator(
    task_id='delete_n_images_task',
    bash_command='/home/priyan/codebase/DatasetBuilder/datasetbuilder-python/src/main/scripts/bash/delete_n_images.sh ',
    dag=dag
)

# Define the task dependencies
delete_small_images_task >> delete_no_face_images_task  >> face_recognition_task >> delete_n_images_task