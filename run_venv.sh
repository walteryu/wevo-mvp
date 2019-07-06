#!/bin/bash

# initiate venv instance:
virtualenv venv --python=`which python3`
source venv/bin/activate

# list list dep in requirements.txt:
pip install -r requirements.txt

# add application path:
export FLASK_APP=app.py
export FLASK_DEBUG=1

# run application; it should open on port 5000:
flask run
