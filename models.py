from app import db
from manage import db, app

# use flask-restless to build api and nest endpoints
# https://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api
from sqlalchemy.ext.declarative\
  import declarative_base, declared_attr
from sqlalchemy\
  import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm\
  import backref, relationship

from wevo-mvp import Base

# model/schema notes:
# 1. declare both here in app.py file
# 2. flask will generate migration files based on logic here
# 3. nested resource declared in child model/schema
# 4. call nested resource from routing, then pass to templates

# nested resource for project/votes
# ref: https://stackoverflow.com/questions/50594051/patching-resources-with-nested-objects-with-flask-sqlalchemy

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

    lat = db.Column(db.String())
    lng = db.Column(db.String())

    # lat/lng optional values as numeric
    # lat = db.Column(db.Numeric(10,4))
    # lng = db.Column(db.Numeric(10,4))

    def __init__(self, name, description, lat, lng):
        self.name = name
        self.description = description
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'lat':self.lat,
            'lng':self.lng
        }

# model and schema class example:
# ref: https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

class ProjectSchema(BaseSchema):
    name = fields.Str()
    description = fields.Str()
    lat = fields.Str()
    lng = fields.Str()

    class Meta(BaseSchema.Meta):
        type_ = 'project'
        model = Project

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# nested resource for project/votes
# ref: https://stackoverflow.com/questions/50594051/patching-resources-with-nested-objects-with-flask-sqlalchemy

class Vote(db.Model):
    id = Column(Integer, primary_key=True) 
    result = db.Column(db.Boolean, default=False, nullable=False) 
    comment = Column(String(255))

    # declare foreign key and parent/child relationship
    project_id = Column(Integer, 
        ForeignKey("project.id"), nullable=True)
    vote = relationship(Project, 
        backref=backref('votes'))

    def __init__(self, result, comment, project_id):
        self.result = result
        self.comment = comment
        self.project_id = project_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'result': self.result,
            'comment': self.comment,
            'project_id':self.project_id
        }

# model and schema class example:
# ref: https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

class VoteSchema(BaseSchema):
    result = fields.Int()
    comment = fields.Str()
    project_id = fields.Int()

    # declare parent schema
    project = fields.Nested('flask_and_restless.schemas.ProjectSchema', many=False)

    class Meta(BaseSchema.Meta):
        type_ = 'vote'
        model = Vote
