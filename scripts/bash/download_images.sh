#!/bin/bash

# This is tested and it worked

# Name of your Conda environment
ENV_NAME="deepface"

CONDA_PATH="$HOME/anaconda3"

LOG_FILE="$HOME/logfiles/download_images.log"

cd ~/codebase/ImageDatasetBuilder/python/src
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"

"$CONDA_PATH/bin/conda" run -n "$ENV_NAME" python3 main/image_downloader/Application.py > "$LOG_FILE" 2>&1