# use flask-restless to build api and nest endpoints
# https://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api
from sqlalchemy.ext.declarative\
  import declarative_base, declared_attr
from sqlalchemy\
  import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm\
  import backref, relationship

from models import Base

# model/schema notes:
# 1. declare both here in app.py file
# 2. flask will generate migration files based on logic here
# 3. nested resource declared in child model/schema
# 4. call nested resource from routing, then pass to templates

# use flask-restless to build api and nest endpoints
# https://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api
class Project(Base):
    @declared_attr
    def __tablename__(cls):
        # API endpoint will take the form '/api/__tablename__'
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    name = Column(String())
    description = Column(String())
    lat = Column(String())
    lng = Column(String())

# use flask-restless to build api and nest endpoints
# https://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api
class Vote(Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    result = Column(Boolean, default=False, nullable=False)
    comment = Column(String(255))

    # declare foreign key and parent/child relationship
    project_id = Column(Integer,
        ForeignKey("project.id"), nullable=True)
    vote = relationship(Project,
        backref=backref('votes'))
