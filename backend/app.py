from flask import Flask
from backend.config import Config

from backend.routes.main_routes import main
from backend.routes.auth_routes import auth

def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    app.config.from_object(Config)
    app.secret_key = app.config.get("SECRET_KEY")

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app