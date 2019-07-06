from typing import List, Dict
from flask import Flask
import mysql.connector
import json

# Dashboard with bokeh
from flask import Flask, render_template, jsonify, request
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models.sources import AjaxDataSource

app = Flask(__name__)

def votes() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'wevo'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM votes')
    results = [
        {project_name: vote} for (project_name, vote, vote_date, lat, lng, comments) in cursor
    ]
    cursor.close()
    connection.close()

    return results

# Experiment with routing:
def data():
    global x
    x += 1
    y = 2**x
    return jsonify(x=x, y=y)

def make_plot():
    plot = figure(plot_height=300, sizing_mode='scale_width')

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2**v for v in x]

    plot.line(x, y, line_width=4)

    script, div = components(plot)
    return script, div

def make_ajax_plot():
    source = AjaxDataSource(data_url=request.url_root + 'data/',
                            polling_interval=2000, mode='append')

    source.data = dict(x=[], y=[])

    plot = figure(plot_height=300, sizing_mode='scale_width')
    plot.line('x', 'y', source=source, line_width=4)

    script, div = components(plot)
    return script, div

@app.route('/')
def index() -> str:
    # return json.dumps({'votes': votes()})

    # Experiment with routing:
    plots = []
    plots.append(make_ajax_plot())
    plots.append(make_plot())

    return render_template('dashboard.html', plots=plots)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
