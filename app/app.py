from flask import Flask
from flask_discord import DiscordOAuth2Session
from dotenv import load_dotenv
import os

from utils.extensions import mysql
from routes import register_routes

discord = DiscordOAuth2Session()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")

    app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
    app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_USER_PASSWORD")
    app.config["MYSQL_DB"] = os.getenv("MYSQL_DATABASE")
    app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")

    app.config["DISCORD_CLIENT_ID"] = os.getenv("DISCORD_CLIENT_ID")
    app.config["DISCORD_CLIENT_SECRET"] = os.getenv("DISCORD_CLIENT_SECRET")
    app.config["DISCORD_REDIRECT_URI"] = os.getenv("DISCORD_REDIRECT_URL")
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true" 

    mysql.init_app(app)
    discord.init_app(app)
    app.discord = discord

    register_routes(app, discord)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)