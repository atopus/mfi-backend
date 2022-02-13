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
        'NAME': 'db'
    }
}
ALLOWED_HOSTS = ['localhost']
```

From command line, move to the `backend` folder and run the development server:

```sh
$ cd backend
$ python manage.py runserver
```
