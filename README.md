# ImageDatasetBuilder

## Introduction

The objective of this process, executed through a series of Python scripts, is to curate an image dataset exclusively containing human images, free from any extraneous elements. 
The procedure starts with downloading images from specified HTML links. 
It proceeds to eliminate images that fall outside the desired size range (100 KB to 5 MB), are corrupted, or do not contain human faces, as determined by facial recognition technology. 
Additionally, images featuring recognizable characters or, optionally, NSFW content are also removed. 
This ensures the dataset is precisely tailored for applications requiring clean and focused human imagery.


## Steps
1. Download images from html links  
2. Delete images not within the size range - > 100kb < 5 mb  
3. Delete corrupt images  
4. Delete images without human faces with deepface  
5. Delete images without human faces with face_recognition  
6. Delete images with characters  
7. Delete images with NSFW content(optional)  

## Setup process
#### setup envs
`
conda create -n img_downloader python=3.10  
conda activate img_downloader   
pip install requests  
pip install Pillow  
conda deactivate
`  
`
conda create -n deepface python=3.10
conda activate deepface
pip install deepface
pip install tf-keras
conda deactivate
`  
`
conda create -n face_recognition python=3.10
conda activate face_recognition
pip install face_recognition
conda deactivate
`  
`
conda create -n deepface python=3.10
conda activate deepface
pip install deepface
pip install tf-keras
conda deactivate
`  
`
conda create -n face_recognition python=3.10
conda activate face_recognition
pip install face_recognition
conda deactivate
`  
`
conda create -n easyocr python=3.10
conda activate easyocr
pip install easyocr
conda deactivate
`  

## Step1 - Download images from html links
### run download script
`
conda activate img_downloader     
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"    
cd ~/codebase/ImageDatasetBuilder/python/src    
python3 main/image_downloader/Application.py    
`
## Step2 - Delete images not within the size range - > 100kb < 5 mb
### run delete script
`
conda activate img_downloader     
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"    
cd ~/codebase/ImageDatasetBuilder/python/src    
python3 main/image_filter/Application.py    
`
## Step3 - delete corrupt images
### run delete corrupt images script
`
conda activate img_downloader     
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"    
cd ~/codebase/ImageDatasetBuilder/python/src    
python3 main/delete_corrupt_images/Application.py   
`
## Step4 - filter images with faces - part1
### run the deepface script
`
conda activate deepface 
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"    
cd ~/codebase/ImageDatasetBuilder/python/src
python3 main/face_filter2/Application.py
`
## Step5 - filter images with faces - part2
### run the script
`
conda activate face_recognition
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"   
cd ~/codebase/ImageDatasetBuilder/python/src
python3 main/face_filter/Application.py
`
## Step6 - Delete images with characters
### run the easyocr script
`
conda activate easyocr  
export PYTHONPATH="~/codebase/ImageDatasetBuilder/python/src:$PYTHONPATH"   
cd ~/codebase/ImageDatasetBuilder/python/src
python3 main/delete_character/Application.py
`
## Step7 (optional, not implemented yet) - Delete images with NSFW content