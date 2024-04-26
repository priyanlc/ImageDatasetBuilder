#!/bin/bash

# Name of your Conda environment
ENV_NAME="img_downloader"

CONDA_PATH="$HOME/anaconda3"

LOG_FILE="$HOME/logfiles/delete_small_images.log"

cd ~/codebase/ImageDatasetBuilder/python/src
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"


"$CONDA_PATH/bin/conda" run -n "$ENV_NAME" python3 main/delete_small/Application.py > "$LOG_FILE" 2>&1

