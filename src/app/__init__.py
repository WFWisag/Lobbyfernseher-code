from flask import Flask

# import the blueprints for the routes

from .views import views
from .auth import auth

with open("src/app/SECRETKEY.txt") as secretkey:
    sk = secretkey.read()


def create_app():
    app = Flask("app")
    app.config["SECRET_KEY"] = sk

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
