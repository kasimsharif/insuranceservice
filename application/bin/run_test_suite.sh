#!/usr/bin/env bash

source .python-version/bin/activate
export ENVIRONMENT=development;
export PYTHONPATH=$PWD;
python application/src/db/manage.py test