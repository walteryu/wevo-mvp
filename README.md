# WeVo Platform - MVP

## We build more inclusive cities with data and analytics.

### Summary

WeVo is a civic engagement platform designed to help land development and building project stakeholders incorporate community feedback into their projects, reduce paper consumption, conserve resources by managing project risk, analyze public sentiment and predict community response.

### Objectives

The project objectives are as follows:

1. Reduce project risk by minimizing project delays and lawsuits
2. Allow constituents to vote on projects and initiatives
3. Allow project owners to track voting and sentiment

### Background

This project started at [Startup Weekend Sacramento](http://communities.techstars.com/usa/sacramento/startup-weekend/14400) in June 2019 with the goal of increasing civic engagement, reducing project risk and helping build more inclusive cities.

### Methodology

This project was developed based on coach feedback and custom development during the event; it pivoted into this concept for the following reasons:

1. Customers have a pain point with costly project delays and lawsuits
2. Constituents may not be involved with the civic engagement process
3. Project owners are required by law to hold public comment periods
4. Project satisfies multiple portions of the sustainability model
5. This project was developed based on the tutorial listed below

## Data Dashboard with Python, Flask and Plotly

### Summary

Initial MVP app with Pythong, Flask and Plotly; it will be developed into the full MVP based on customer interviews with additional features. User authentication, CRUD operations, voting feature and data visualization will be added soon.

### Local Development

1. Verify that Python and Pip (package manager) have been installed
* 1.1. Production runs on Python 3; however, either v2 or 3 works in dev mode
2. After verifying installations, git clone this repository
* 1.2. Repository contains dev branch for collaboration
3. From within the root directory, run commands within `scripts/venv_notes.sh`
* 3.1. File has instructions for creating virtual environment for packages
* 3.2. Instructions will download required packages and start local server
4. Local database currently is SQLite, and deployment database is Postgres
* 4.1. Database settings identified within config.py file
* 4.2. Models.py file contain data schema; manage.py contains migration info
* 4.3. Create migration files with `python manage.py db init`
* 4.4. Move migration files with `python manage.py db migrate`
* 4.5. Execute migration files with `python manage.py db upgrade`

### Heroku Deployment

1. Procfile, requirements.txt and runtime.txt files provide necessary info
* 1.1. Procfile creates 1 web worker with gunicorn
* 1.2. Python 3 is specified in runtime.txt file
2. Verify that Heroku toolbelt is installed, then add Heroku as remote
* 2.1. Verify that all changes are committed and stored on the master branch
* 2.2. Check that config vars have been set and app created in Heroku dashboard
3. Next, deploy using `git push heroku master` once repo has been linked

### Citations

MVP is based on the tutorials and links below:

Flask, Postgres and Heroku:
* MVP closely follows this [tutorial](https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc)
* Tutorial [Github Repo](https://github.com/dushan14/books-store)
* Real Python [tutorial](https://realpython.com/flask-by-example-part-1-project-setup/) which has more complex features but first several sections are useful
* Flask [documentation](http://flask.pocoo.org/docs/1.0/patterns/#patterns) which has design patterns for common tasks such as database, MVC and template design

Data Dashboard with Plotly:
* Hepta Analytics [Tutorial](https://blog.heptanalytics.com/2018/08/07/flask-plotly-dashboard/)
* Hepta Analytics [Github Repo](https://github.com/yvonnegitau/flask-Dashboard)
* Plotly [website](https://plot.ly/products/dash/) with additional documentation
