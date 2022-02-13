# Peak API

This repo is used as the backend part of the [peaks app](https://github.com/atopus/mfi-test).

## Development

Add a `localsettings.py` file in the `backend/backend` folder, with the following variables as an illustration:

```py
ENV = 'development'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}
ALLOWED_HOSTS = ['localhost']
```

From command line, move to the `backend` folder, add a virtual environment, load the dependencies and run the development server:

```sh
$ cd backend
$ python -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata data.yaml # Optional: load the data extracted from the peak source data.
$ python manage.py runserver
```

The application should be accessible at http://localhost:8000/api/peaks.

The admin django server should be accessible at http://localhost:8000/admin.

## Data

The [peak sources github repo](https://github.com/open-peaks/data) has been used to populate the database.
