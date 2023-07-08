from flask import Flask
from . import views


def create_app():
    app = Flask("app")
    app.config["SECRET_KEY"] = "b'P\x98\x91\xec\xc2?\xee\x9d\xe9\xb8W\x1a'"

    app.register_blueprint(views.views, url_prefix="/")
    return app
