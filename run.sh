#!/bin/bash
echo "Starts backend server."
exec python manage.py "$@"