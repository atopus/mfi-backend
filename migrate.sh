#!/bin/bash
python manage.py migrate
python manage.py loaddata ./data.yaml
uwsgi --ini /code/test_uwsgi.ini