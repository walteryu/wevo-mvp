#!/bin/bash

# run migrations locally
# python manage.py db init
python manage.py db migrate
python manage.py db upgrade
