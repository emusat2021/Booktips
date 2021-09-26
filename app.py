import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash    
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if request.form.get("password") != request.form.get("confirm_password"):
            flash("Passwords do not match")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }

        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Your account has been successfully created!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_books"))
            else:
                # invalid password match
                flash("Incorect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username do not exist
            flash("Incorect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/view/<username>", methods=["GET", "POST"])
def profile(username):
    if session["user"]:
        # retrieve user id from the DB
        user_id = mongo.db.users.find_one(
            {"username": username})["_id"]
        # edit profile action save
        if request.method == "POST":
            # update the DB

            profile_data = {
                "user_email": request.form.get("email").lower(),
                "user_firstname": request.form.get("first_name").lower().capitalize(),
                "user_lastname": request.form.get("last_name").lower().capitalize(),
                "img_url": request.form.get("img_url"),
                "user_id": user_id,
            }
            # update profile for the username in the DB
            mongo.db.profiles.update({"user_id": ObjectId(user_id)}, profile_data)

            flash("Your profile has been successfully updated!")
        # GET method
        # retrieve user profile from the DB
        user_profile = mongo.db.profiles.find_one(
            {"user_id": user_id})

        data_template = {
            "user_email": user_profile["user_email"],
            "user_firstname": user_profile["user_firstname"],
            "user_lastname": user_profile["user_lastname"],
            "img_url": user_profile["img_url"],
            "username": username,
        }
        return render_template("profile.html", data_template=data_template)
        

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
        