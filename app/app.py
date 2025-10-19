from flask import Flask, render_template, request, jsonify
import requests
import json, os
from dotenv import load_dotenv
from flask_mysqldb import MySQL

app = Flask(__name__)
load_dotenv()

app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DATABASE")
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/api/chat', methods=["POST"])
def chat():
    data = request.get_json()
    query = {
        'model': 'BaseModel',
        'messages': data["messages"]
    }
    r = requests.post('http://127.0.0.1:8080/chat/completions', data=json.dumps(query), headers={'Content-Type': 'application/json'})
    r = json.loads(r.content)
    data_to_return = {
        'created': r["created"],
        'usage': r["usage"],
        'message': r["choices"][0]["message"]["content"]
    }
    return jsonify(data_to_return)