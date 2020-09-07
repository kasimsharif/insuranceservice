#!/usr/bin/env bash


#### Creating virtual environment ##########
virtualenv -p python3 .python-version
source .python-version/bin/activate

echo "Created virtual environment "

echo "Install requirements.txt"
pip install -r requirements.txt

echo "Installed the requirements"

