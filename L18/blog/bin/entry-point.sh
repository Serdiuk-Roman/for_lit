#! /bin/bash

pip install --upgrade pip
python manage.py migrate
python manage.py runserver
