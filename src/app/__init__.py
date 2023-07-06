from flask import Flask
from . import views


def create_app():
    app = Flask("app")

    app.register_blueprint(views.views, url_prefix="/")
    return app
