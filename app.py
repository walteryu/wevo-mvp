import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# dashboard plotting packages
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

app = Flask(__name__)

# import app and db settings
app.config.from_object(os.environ['APP_SETTINGS'])
# app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
db.init_app(app)

# import db schema
from models import Project

# homepage dashboard route
@app.route('/')
def index():
    feature = 'Bar'
    bar = create_plot(feature)
    return render_template('index.html', plot=bar)

def create_plot(feature):
    if feature == 'Bar':
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'], # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]
    else:
        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        data = [go.Scatter(
            x = random_x,
            y = random_y,
            mode = 'markers'
        )]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

# homepage dashboard route
@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    feature = request.args['selected']
    graphJSON= create_plot(feature)
    return graphJSON

# project crud/api route
@app.route("/details")
def get_project_details():
    name=request.args.get('name')
    description=request.args.get('description')
    lat=request.args.get('lat')
    lng=request.args.get('lng')
    return "Description: {}, Lat: {}, Lng: {}".format(description, lat, lng)

# project crud/api route
@app.route("/get/projects")
def get_projects():
    try:
        projects=Project.query.all()
        return jsonify([e.serialize() for e in projects])
    except Exception as e:
	    return(str(e))

# project crud/api route
@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        project=Project.query.filter_by(id=id_).first()
        return jsonify(project.serialize())
    except Exception as e:
	    return(str(e))

# project crud method
def add_project():
    name=request.args.get('name')
    description=request.args.get('description')
    lat=request.args.get('lat')
    lng=request.args.get('lng')
    try:
        project=Project(
            name=name,
            description=description,
            lat=lat,
            lng=lng
        )
        db.session.add(project)
        db.session.commit()
        return "Project added. project id={}".format(project.id)
    except Exception as e:
	    return(str(e))

# project crud route
@app.route("/project/new",methods=['GET', 'POST'])
def add_project_form():
    if request.method == 'POST':
        name=request.form.get('name')
        description=request.form.get('description')
        lat=request.form.get('lat')
        lng=request.form.get('lng')
        try:
            project=Project(
                name=name,
                description=description,
                lat=lat,
                lng=lng
            )
            db.session.add(project)
            db.session.commit()
            return "Project added! project id={}".format(project.id)
        except Exception as e:
            return(str(e))
    return render_template("project_new.html")

# project crud route
@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template("projects.html",
                           title="Projects",
                           projects=projects)

if __name__ == '__main__':
    app.run()
