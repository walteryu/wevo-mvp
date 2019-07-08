#!/bin/bash

# initiate virtualenv so that packages stay within it:
virtualenv venv --python=`which python3`
source venv/bin/activate

# install all packages within requirements.txt:
pip install -r requirements.txt

# add application path to start it; set to dev mode:
export FLASK_APP=app.py
export FLASK_DEBUG=1

# run application; it opens on port 5000:
flask run
