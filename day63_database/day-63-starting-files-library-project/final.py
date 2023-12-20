import flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

# create table name
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


# create table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Read all records
    with app.app_context():
        all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        book_rating = request.form['book_rating']
        # CREATE RECORD
        with app.app_context():
            new_book = Book(title=book_name, author=book_author, rating=book_rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect("/")
    return render_template("add.html")





if __name__ == "__main__":
    app.run(debug=True)

