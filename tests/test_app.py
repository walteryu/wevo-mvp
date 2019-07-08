import os
import tempfile
import pytest
import flask

from flask import app

@pytest.fixture
def app():
    app = create_app()
    return app

def client():
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()

    with flaskr.app.app_context():
        flaskr.init_db()

    yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data

def test_example(client):
    response = client.get("/")
    assert response.status_code == 200
