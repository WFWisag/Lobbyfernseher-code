from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
import os
import json

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


filetypes = ["png", "jpg", "jpeg"]  # TODO: add video support later


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in filetypes


@views.route("/admin/sliderconfig", methods=["GET", "POST"])
@login_required
def config():
    if request.method == "POST":
        # duration handling
        duration = request.form.get("duration")
        if duration:
            with open("src/app/data/slider.json", "r+") as f:
                data = json.load(f)
                data["duration"] = duration
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        # Fileupload handling
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if allowed_file(file.filename):
            file.save(os.path.join("src/app/uploads", file.filename))
            with open("src/app/data/slider.json", "r+") as f:
                data = json.load(f)
                data["media"].append(file.filename)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            return redirect(request.url)

    files = os.listdir("src/app/uploads")
    return render_template("config.html", files=files)


@views.route("/admin/sliderconfig/delete/<filename>")
@login_required
def delete(filename):
    os.remove(os.path.join("src/app/uploads", filename))
    with open("src/app/data/slider.json", "r+") as f:
        data = json.load(f)
        data["media"].remove(filename)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    return redirect(url_for("views.config"))


@views.route("/slider")
@login_required
def slider():
    return render_template("slider.html")
