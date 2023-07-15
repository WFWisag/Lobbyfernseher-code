from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

views = Blueprint("views", __name__)


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if "logged_in" in session:
            return view_func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))

    return wrapped_view


@views.route("/")
def home():
    return redirect(url_for("auth.login"))


@views.route("/admin/panel")
@login_required
def panel():
    return render_template("panel.html")


@views.route("/admin/panel/config")
@login_required
def config():
    return render_template("config.html")


@views.route("/slider")
@login_required
def slider():
    return render_template("slider.html")
