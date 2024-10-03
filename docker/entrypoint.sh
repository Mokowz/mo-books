#!/usr/bin/env bash
python manage.py makemigrations account books

python manage.py migrate --no-inputs

python manage.py collectstatic

python manage.py runserver