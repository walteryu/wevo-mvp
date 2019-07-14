#!/bin/bash

# run migrations locally
# python3 manage.py db init

# indicate current state
# python3 manage.py db stamp heads

# migrate and upgrade db
python3 manage.py db migrate
python3 manage.py db upgrade
