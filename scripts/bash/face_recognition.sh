#!/bin/bash

# Name of your Conda environment
ENV_NAME="face_recognition"

CONDA_PATH="$HOME/anaconda3"

LOG_FILE="/home/priyan/logfiles/delete_no_face_with_face_recognition.log"

cd ~/codebase/ImageDatasetBuilder/python/src
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"

"$CONDA_PATH/bin/conda" run -n "$ENV_NAME" python3 main/face_recognition/Application.py > "$LOG_FILE" 2>&1