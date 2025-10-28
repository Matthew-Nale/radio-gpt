from flask import Blueprint, session, redirect, url_for, render_template, current_app
from flask_discord import Unauthorized

from utils.sql import store_discord_tokens
from utils.auth_utils import requires_whitelisted

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return current_app.discord.create_session()

@auth.route("/callback")
def callback():
    current_app.discord.callback()

    user = current_app.discord.fetch_user()
    discord_tokens = session.get('DISCORD_OAUTH2_TOKEN')

    session["user_id"] = user.id
    session["discord_username"] = user.username
    session["logged_in"] = True

    store_discord_tokens(
        user.id,
        user.username,
        user.avatar_url,
        discord_tokens["access_token"],
        discord_tokens["refresh_token"],
        discord_tokens["expires_in"]
    )

    return redirect(url_for("auth.query"))


@auth.route("/chat")
@requires_whitelisted
def query():
    return render_template("query.html")


@auth.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for("main.index"))