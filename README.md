# Insurance Service

CRUD API for Insurance service <br><br>
Postman link : https://www.getpostman.com/collections/26d7bef975d72dfbc382
# Pre requisite
1. Install Python 3.7
2. Install virtualenv

# Project Setup using scripts

1. Setup the project.

```
$ ./application/bin/setup.sh
```

2. Run the application.

```
$ ./application/bin/run.sh
```

3. To run the test suite.

```
$ ./application/bin/run_test_suite.sh
```


# To manually setup the project 

1. Create and activate your virtual env.
```
$ virtualenv -p python3 .python-version
$ source .python-version/bin/activate
```

2. Install requirements.txt
```
$ python install -r requirements.txt
```

4. Run the integration tests by:
```
$ export ENVIRONMENT=development; export PYTHONPATH=$PWD
$ python application/tests/it/test_insurance_policy.py
```

5. Run application by:
```
$ export ENVIRONMENT=development; export PYTHONPATH=$PWD
$ python application/src/launcher.py
```
