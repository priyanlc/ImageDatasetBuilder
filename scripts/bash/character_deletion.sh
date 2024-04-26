#!/bin/bash

# Name of your Conda environment
# This is tested and it worked
ENV_NAME="easyocr"

CONDA_PATH="$HOME/anaconda3"

LOG_FILE="$HOME/logfiles/delete_character.log"

cd ~/codebase/ImageDatasetBuilder/python/src
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"

"$CONDA_PATH/bin/conda" run -n "$ENV_NAME" python3 main/delete_character/Application.py > "$LOG_FILE" 2>&1