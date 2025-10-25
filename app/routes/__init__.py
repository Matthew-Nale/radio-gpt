from .main import main
from .auth import auth
from .api import api

def register_routes(app, discord):
    app.discord = discord

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api)