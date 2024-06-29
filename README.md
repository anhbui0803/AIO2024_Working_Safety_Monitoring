# YOLOv10 Streamlit Demo

## Description
Helmet Detection web demo using YOLOv10 and Streamlit.

## How to use
### Option 1: Using conda environment
1. Create new conda environment and install required dependencies:
```
$ conda create -n <env_name> -y python=3.11
$ conda activate <env_name>
$ pip3 install -r requirements.txt
```
2. Host streamlit app
```
$ streamlit run app.py
```
### Option 2: Using pip virtualenv
1. Create new pip virtual environment and install required dependencies:

If you don't have virtualenv, please install via pip: 
```
$ python -m pip install --user virtualenv
```
```
$ virtualenv <env_name>
$ <env_name>\Scripts\activate
# python -m pip install -r requirements.txt
```
2. Host streamlit app
```
$ python -m streamlit run app.py
```
