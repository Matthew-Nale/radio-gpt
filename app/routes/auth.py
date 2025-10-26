from flask import Blueprint, session, redirect, url_for, render_template, current_app
from flask_discord import requires_authorization, Unauthorized

from functools import wraps

from utils.sql import store_discord_tokens, is_whitelisted

auth = Blueprint("auth", __name__)


def requires_registration(f):
    @wraps(f)
    @requires_authorization
    def decorated(*args, **kwargs):
        user_id, username = session.get("user_id"), session.get("discord_username")

        if not user_id:
            return redirect(url_for("auth.login"))
        
        if not is_whitelisted(user_id, username):
            return "You are not authorized to access this page", 403
    
        return f(*args, **kwargs)
    return decorated


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
@requires_registration
def query():
    return render_template("query.html")


@auth.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for("main.index"))