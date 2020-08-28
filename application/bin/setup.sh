#!/usr/bin/env bash


##### Creating Database ########
mysql -u$DB_USER -p$DB_PASSWORD << EOF
drop database insurance;
create database $DB_NAME;
exit
EOF

echo "Database '$DB_NAME' created successfully.."

#### Creating virtual environment ##########
virtualenv -p python3 .python-version
source .python-version/bin/activate

echo "Created virtual environment "

echo "Install requirements.txt"
pip install -r requirements.txt

###### Run Python migration #########

echo "DB Migration started"
export ENVIRONMENT=development
export DJANGO_SETTINGS_MODULE=application.src.db.settings.development
export PYTHONPATH=$PWD

python application/src/db/manage.py migrate

echo "Migration completed"

