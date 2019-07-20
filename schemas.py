# use flask-restless to build api and nest endpoints
# https://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api

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
