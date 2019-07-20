from app import db
from manage import db, app

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

# nested resource for project/votes
# ref: https://stackoverflow.com/questions/50594051/patching-resources-with-nested-objects-with-flask-sqlalchemy
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Boolean, default=False, nullable=False)
    comment = db.Column(db.String(255))

    # declare foreign key and parent/child relationship
    project_id = db.Column(db.Integer,
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
