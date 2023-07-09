from flask import Flask
from . import views

with open('SECRETKEY.txt') as secretkey:
    sk = secretkey


def create_app():
    app = Flask("app")
    app.config["SECRET_KEY"] = sk

    app.register_blueprint(views.views, url_prefix="/")
    return app
