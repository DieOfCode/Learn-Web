import json
from flask import Blueprint, render_template, session, request, url_for, redirect
from models.user import User, UserErrors

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            User.register_user(email, password)
            session["email"] = email
            return email
        except UserErrors as e:
            return e.message
    return render_template("users/register.html")


@user_blueprint.route("/login", methods=["GET", "POST"])
def login_user():
    if request.form == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            if User.is_login_valid(email, password):
                session["email"] = email
                return email
        except UserErrors.UserError as e:
            return e.message
    return render_template("users/login.html")

@user_blueprint.route("/logout")
def logout():
    session["email"] = None
    return redirect(".user_login")
