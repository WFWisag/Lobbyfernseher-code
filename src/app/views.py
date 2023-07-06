from flask import Blueprint, render_template, request, redirect, url_for, flash

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return redirect("/admin/login")


# TODO: when logged in, redirect to /admin/panel


@views.route("/admin/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


# TODO: add login functionality


@views.route("/admin/panel")
def panel():
    pass


@views.route("/admin/panel/config")
def config():
    pass


@views.route("/slider")
def slider():
    return render_template("slider.html")
