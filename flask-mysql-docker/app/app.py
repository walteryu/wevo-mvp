from typing import List, Dict
from flask import Flask
import mysql.connector
import json

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

@app.route('/')
def index() -> str:
    return json.dumps({'votes': votes()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
