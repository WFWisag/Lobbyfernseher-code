from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return redirect(url_for("auth.login"))


@views.route("/admin/panel")
def panel():
    return render_template("panel.html")


@views.route("/admin/panel/config")
def config():
    return render_template("config.html")


@views.route("/slider")
def slider():
    return render_template("slider.html")
