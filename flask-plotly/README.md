# WeVo Platform MVP

## Data Dashboard with Flask and Plotly

## Summary

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

* Hepta Analytics [Tutorial](https://blog.heptanalytics.com/2018/08/07/flask-plotly-dashboard/)
* Hepta Analytics [Github Repo](https://github.com/yvonnegitau/flask-Dashboard)
