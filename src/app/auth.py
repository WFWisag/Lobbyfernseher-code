from flask import Blueprint, render_template, request, redirect, url_for
from .loginsystem import check_login

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form

    if request.method == "POST":
        username = data.get("username")
        password = data.get("password")

        if check_login(username, password):
            return redirect(
                url_for("views.panel")
            )  # TODO: change this to the dashboard page
        else:
            return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "logout"
