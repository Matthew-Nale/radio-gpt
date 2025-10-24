from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mysqldb import MySQL
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
from dotenv import load_dotenv

import requests
import json, os

app = Flask(__name__)
load_dotenv()

app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_USER_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DATABASE")
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")

app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
app.config["DISCORD_CLIENT_ID"] = os.getenv("DISCORD_CLIENT_ID")
app.config["DISCORD_CLIENT_SECRET"] = os.getenv("DISCORD_CLIENT_SECRET")
app.config["DISCORD_REDIRECT_URI"] = os.getenv("DISCORD_REDIRECT_URL")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true" 

mysql = MySQL(app)
discord = DiscordOAuth2Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return discord.create_session()

@app.route("/callback")
def callback():
    discord.callback()
    return redirect(url_for("query"))

@app.route("/chat")
@requires_authorization
def query():
    return render_template('query.html')

@app.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for("login"))

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