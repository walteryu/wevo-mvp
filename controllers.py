# use flask-restless to build api and nest endpoints
# https://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api

from app import app, s, manager
from models import Project, Vote

project_api_blueprint = manager.create_api_blueprint(Project,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])
vote_api_blueprint = manager.create_api_blueprint(Vote,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])
