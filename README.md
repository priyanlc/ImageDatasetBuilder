# ImageDatasetBuilder

## download images
### setup env
conda create -n img_downloader python=3.10  
conda activate img_downloader  
pip install requests  

### run download script
conda activate img_downloader  
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"
cd ~/codebase/ImageDatasetBuilder/python/src
python3 main/image_downloader/Application.py
