from app import db
from manage import db, app

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

    # TODO: run migration for lat/lng:
    lat = db.Column(db.String())
    lng = db.Column(db.String())
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
