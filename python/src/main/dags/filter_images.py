from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# scheduled once every 10 mins
dag = DAG(
    'filter_images',
    description='Run scripts to remove bad images DAG',
    start_date=datetime(2023, 3, 22),
    schedule_interval='*/30 * * * *',
    catchup=False
)

deep_face_task = BashOperator(
    task_id='deep_face_filter_task',
    bash_command='~/codebase/ImageDatasetBuilder/scripts/bash/deep_face.sh ',
    dag=dag
)

face_recognition_task = BashOperator(
    task_id='face_recognition_filter_task',
    bash_command='~/codebase/ImageDatasetBuilder/scripts/bash/face_recognition.sh ',
    dag=dag
)

delete_character_task = BashOperator(
    task_id='character_deletion_task',
    bash_command='~/codebase/ImageDatasetBuilder/scripts/bash/character_deletion.sh ',
    dag=dag
)

deep_face_task >> face_recognition_task >> delete_character_task