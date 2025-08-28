from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os


DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    'books-collection.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Base(DeclarativeBase):
    pass

class Book(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), unique=True, nullable=False)
    author = db.Column(String(250), nullable=False)
    rating = db.Column(Float, nullable=False)


@app.route('/', methods=["GET", "POST"])
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("book_title")
        author = request.form.get("book_author")
        rating = float(request.form.get("book_rating"))
        
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

with app.app_context():
    db.create_all()
