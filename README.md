# Insurance Service

CRUD API for Insurance service

# Pre requisite
1. Install Python 3.7
2. Install virtualenv

# Project Setup

1. Create and activate your virtual env.
```
$ virtualenv -p python3 .python-version
$ source .python-version/bin/activate
```

2. Install requirements.txt
```
$ python install -r requirements.txt
```

3. Create database "insurance"

```
$ mysql -u root -p
$ mysql> create database insurance
```

4. export DATABASE variables
```
$ export DB_NAME=insurance
$ export DB_USER=root
$ export DB_PASSWORD=test@123
```

4. Run the integration tests by:
```
$ export ENVIRONMENT=development;export DJANGO_SETTINGS_MODULE=application.src.db.settings.development; export PYTHONPATH=$PWD
$ python application/src/db/manage.py test
```
5. Run the Django migrations:
```
$ export ENVIRONMENT=development;export DJANGO_SETTINGS_MODULE=application.src.db.settings.development; export PYTHONPATH=$PWD
$ python application/src/db/manage.py migrate
```

5. Run application by:
```
$ export ENVIRONMENT=development;export DJANGO_SETTINGS_MODULE=application.src.db.settings.development; export PYTHONPATH=$PWD
$ python application/src/launcher.py
```
