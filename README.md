# Test-Driven Development with Django, Django REST Framework, and Docker

[![pipeline status](https://gitlab.com/davidgranados1/dg-django-ecommerce/badges/main/pipeline.svg)](https://gitlab.com/davidgranados1/dg-django-ecommerce/commits/main)





## Pytest

### normal run
$ docker-compose exec app pytest

### disable warnings
$ docker-compose exec app pytest -p no:warnings

### run only the last failed tests
$ docker-compose exec app pytest --lf

### run only the tests with names that match the string expression
$ docker-compose exec app pytest -k "movie and not all_movies"

### stop the test session after the first failure
$ docker-compose exec app pytest -x

### enter PDB after first failure then end the test session
$ docker-compose exec app pytest -x --pdb

### stop the test run after two failures
$ docker-compose exec app pytest --maxfail=2

### show local variables in tracebacks
$ docker-compose exec app pytest -l

### list the 2 slowest tests
$ docker-compose exec app pytest  --durations=2

### Run the tests with coverage:
$ docker-compose exec app pytest -p no:warnings --cov=.

### Run the tests with coverage and html version:
$ docker-compose exec app pytest -p no:warnings --cov=. --cov-report html

