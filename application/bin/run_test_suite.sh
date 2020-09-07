#!/usr/bin/env bash

source .python-version/bin/activate
export ENVIRONMENT=development;
export PYTHONPATH=$PWD;
python application/tests/it/test_insurance_policy.py