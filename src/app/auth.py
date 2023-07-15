from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
)

from .loginsystem import check_login

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form

    if request.method == "POST":
        username = data.get("username")
        password = data.get("password")

        if check_login(username, password):
            session["username"] = username
            session["password"] = password
            session["logged_in"] = True

            return redirect(url_for("views.panel"))
        else:
            return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("password", None)
    session.pop("logged_in", False)
    return redirect(url_for("auth.login"))
