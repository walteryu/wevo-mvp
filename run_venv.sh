#!/bin/bash

# Create and run venv and requirements.txt
virtualenv venv --python=`which python3`
source venv/bin/activate
# pip install Flask bokeh
# mkdir templates
# touch app.py
export FLASK_APP=app.py
export FLASK_DEBUG=1

pip install -r requirements.txt
flask run
