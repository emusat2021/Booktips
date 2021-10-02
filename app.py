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
    """
    This route displays a list of all books
    from database in home webpage.
    """
    books = list(mongo.db.books.find().sort("book_title", 1))
    return render_template("books.html", books=books)

@app.route("/book/view/<book_id>")
def book_view(book_id):
    # check if the given book id is valid mongodb object id
    if ObjectId.is_valid(book_id):
        book = mongo.db.books.find_one(
            {"_id": ObjectId(book_id)})
    
        # read/search in MongoDB for all reviews for a specific book id
        reviews = list(
            mongo.db.reviews.find({"book_id": ObjectId(book_id)})
        )
        # idea taken from https://stackoverflow.com/questions/14071038/add-an-element-in-each-dictionary-of-a-list-list-comprehension
        # add 2 new keys to each dictionary in list reviews
        for review in reviews:

            img_url_em = mongo.db.profiles.find_one({"user_id": review["user_id"]})["img_url"]
            username_em = mongo.db.users.find_one({"_id": review["user_id"]})["username"]

            review.update({
                "img_url": img_url_em,
                "username": username_em,
            })


    else:
        book = None

    return render_template("book_view.html", book=book, reviews=reviews, )


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """
    This route adds a new book in the database.
    It has two methods: GET and POST.
    GET method displays a form for user to fill in.
    POST method adds the book in the database and then 
    redirects user to home page.
    This function can only be used by an authenticated user.
    """
    if session.get("user"):
        if request.method == "POST":
            # collect data from form and build document in collection books in MongoDB
            user_id = mongo.db.users.find_one(
                {"username": session["user"]})["_id"]
            book_data = {
                "book_title": request.form.get("book_title"),
                "book_author_name": request.form.get("book_author_name"),
                "book_cover_url": request.form.get("book_cover_url"),
                "book_isbn": request.form.get("book_isbn"),
                "book_description": request.form.get("book_description"),
                "user_id": user_id,
            }
            # insert the document into the database
            mongo.db.books.insert_one(book_data)
            return redirect(url_for("get_books"))

        if request.method == "GET":
            return render_template("action_book.html", book=id)

    flash("You must be authenticated in order to add books!")
    return redirect(url_for("get_books"))


@app.route("/add_review/<book_id>", methods=["GET", "POST"])
def add_review(book_id):
    if session.get("user"):
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        
        # search for a review of the current book and the current user
        review_db = mongo.db.reviews.find_one({
            "book_id": ObjectId(book_id),
            "user_id": user_id,
        })
        # if user has already review on the respective book then rediret to edit
        if review_db:
            return redirect(url_for("edit_review", book_id=book_id))


        if request.method == "GET":
            # read book details from DB
            book = mongo.db.books.find_one(
                {"_id": ObjectId(book_id)})
        
            return render_template("action_review.html", book=book, review_j2=review_db, source_route="add")

        if request.method == "POST":


            # object to be put in MongoDB(structure of a document in collection reviews)
            user_review = {
                "review_text": request.form.get("user_review"),
                "user_id": user_id,
                "book_id": ObjectId(book_id),
            }
            # insert the document into the database
            mongo.db.reviews.insert_one(user_review)
            return redirect(url_for("get_books"))

    else:
        flash("You must be authenticated in order to add reviews!")
        return redirect(url_for("get_books"))


@app.route("/edit_review/<book_id>", methods=["GET", "POST"])
def edit_review(book_id):
    if session.get("user"):
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]

        if request.method == "GET":
            # read book details from DB
            book = mongo.db.books.find_one(
                {"_id": ObjectId(book_id)})
            
            # search using a filter for a review of the current book and the current user
            review_db = mongo.db.reviews.find_one({
                "book_id": ObjectId(book_id),
                "user_id": user_id,
            })
            
            return render_template("action_review.html", book=book, review_j2=review_db, source_route="edit")

        if request.method == "POST":

            # object to be put in MongoDB(structure of a document in collection reviews)
            update_user_review = {
                "review_text": request.form.get("user_review"),
                "user_id": user_id,
                "book_id": ObjectId(book_id),
            }
            # update the document into the database
            mongo.db.reviews.update({
                "user_id": user_id,
                "book_id": ObjectId(book_id),
            }, update_user_review)
            return redirect(url_for("book_view", book_id=book_id))

    else:
        flash("You must be authenticated in order to edit reviews!")
        return redirect(url_for("get_books"))


@app.route("/delete_review/<book_id>")
def delete_review(book_id):
    """
    Delete review.
    First we check user's authentication.
    Then delete.
    """
    if session.get("user"):
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        # filter on book id and specific user id
        mongo.db.reviews.remove({
            "book_id": ObjectId(book_id),
            "user_id": user_id,
            })

        flash("Review Successfully Deleted")
        return redirect(url_for("profile", username=session["user"]))
    else:
        flash("You must be authenticated in order to delete reviews!")
        return redirect(url_for("get_books"))   


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        books = list(mongo.db.books.find({"$text": {"$search": query}}))
        return render_template("books.html", books=books)
    return redirect(url_for("get_books"))


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

        # build document to insert into MongoDB
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        # insert the document into the database
        mongo.db.users.insert_one(register)

        # retrieve user id from the DB
        user_id = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})["_id"]
        # build document to insert into MongoDB
        profile_data = {
            "user_email": "",
            "user_firstname": "",
            "user_lastname": "",
            "img_url": "https://s.gr-assets.com/assets/nophoto/user/u_111x148-9394ebedbb3c6c218f64be9549657029.png",
            "user_id": user_id,
        }
        # insert the document into the database
        mongo.db.profiles.insert_one(profile_data)

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
    if session.get("user"):
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
        # find all books created by the current user
        books = list(mongo.db.books.find({"user_id": user_id}).sort("book_title", 1))
        # find all reviews created by the current user
        reviews = list(mongo.db.reviews.find({"user_id": user_id}))

        # add details/title about the respective book in each review
        for review in reviews:
            book_info_em = mongo.db.books.find_one({"_id": review["book_id"]})

            review.update({
                "book_title": book_info_em["book_title"],
            })
        return render_template("profile.html", data_template=data_template, books=books, reviews=reviews)
        

    return redirect(url_for("login"))


@app.route("/profile/edit/<username>")
def profile_edit(username):
    user_id = mongo.db.users.find_one(
        {"username": username})["_id"]
    user_profile = mongo.db.profiles.find_one(
        {"user_id": user_id})

    data_template = {
        "user_email": user_profile["user_email"],
        "user_firstname": user_profile["user_firstname"],
        "user_lastname": user_profile["user_lastname"],
        "img_url": user_profile["img_url"],
        "username": username,
    }

    return render_template("profile_edit.html", data_template=data_template)


@app.route("/profile/delete/<username>")
def profile_delete(username):
    flash("Your account has been deleted!")
    session.pop("user", None)
    return redirect(url_for("get_books"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user", None)
    return redirect(url_for("get_books"))
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
        