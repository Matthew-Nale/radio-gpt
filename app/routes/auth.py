from flask import Blueprint, session, redirect, url_for, render_template, current_app
from flask_discord import requires_authorization, Unauthorized
from utils.sql import store_discord_tokens

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    print(session)
    return current_app.discord.create_session()

@auth.route("/callback")
def callback():
    current_app.discord.callback()

    user = current_app.discord.fetch_user()
    discord_tokens = session.get('DISCORD_OAUTH2_TOKEN')

    session["discord_username"] = user.username
    session["logged_in"] = True

    return redirect(url_for("auth.query"))

@auth.route("/chat")
@requires_authorization
def query():
    return render_template("query.html")

@auth.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for("auth.login"))