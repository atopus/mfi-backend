#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata ./data.yaml
uwsgi --ini /code/deploy/mfi_uwsgi.ini