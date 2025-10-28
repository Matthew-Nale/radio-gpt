from functools import wraps
from flask_discord import requires_authorization
from flask import session, redirect, url_for

from utils.sql import is_whitelisted

def requires_whitelisted(f):
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
