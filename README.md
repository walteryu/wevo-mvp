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

## Data Dashboard with Flask and Plotly

### Summary

Initial MVP app with Flask and Plotly; it will be developed into the full MVP based on customer interviews with additional features. User authentication, CRUD operations, voting feature and data visualization will be added soon.

### Local Installation

1. Verify that Python and Pip have been installed
2. After installations, git clone this repository
3. From within the root directory, run commands within `./run_venv.sh`
4. Commands will create and start virtualvenv instance
* 4.1. Next, install packages within requirements.txt
* 4.2. Once installed, then start app with `flask run`

### Heroku Deployment

1. Procfile, requirements.txt and runtime.txt files provide necessary info
2. Verify that Heroku toolbelt is installed, then add Github repo to application
3. Next, deploy using `git push heroku master` once repo has been linked

### Citations

MVP is based on the links below:

Data Dashboard with Plotly:
* Hepta Analytics [Tutorial](https://blog.heptanalytics.com/2018/08/07/flask-plotly-dashboard/)
* Hepta Analytics [Github Repo](https://github.com/yvonnegitau/flask-Dashboard)

Postgres, Data Model and Migrations:
* Medium Article [Tutorial](https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc)
* Tutorial [Github Repo](https://github.com/dushan14/books-store)
