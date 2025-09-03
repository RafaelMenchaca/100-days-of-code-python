from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

# Database file path
DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    'movies.db'
)


load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap5(app)
db = SQLAlchemy(app)

# Movie table
class Movie(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), unique=True, nullable=False)
    year = db.Column(String(250), nullable=False)
    description = db.Column(String(500), nullable=False)
    rating = db.Column(Float, nullable=True)
    ranking = db.Column(Integer, nullable=True)
    review = db.Column(String(250), nullable=True)
    img_url = db.Column(String(250), nullable=False)

class EditMovieForm(FlaskForm):
    rating = StringField("Your Rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# Sample movies
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

@app.route("/")
def home():
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.rating.desc())
    ).scalars().all()
    for i in range(len(movies)):
        movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = db.session.get(Movie, id)
    form = EditMovieForm()

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.get(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={"api_key": API_KEY, "query": movie_title}
        )
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

# Select movie from search results
@app.route("/add/<int:movie_id>")
def add_movie(movie_id):
    # get the movie details
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}",
        params={"api_key": API_KEY}
    )
    data = response.json()
    # create a new movie object
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    # add the movie to the database
    db.session.add(new_movie)
    db.session.commit()
    # redirect to the edit page to add rating and review
    return redirect(url_for('edit', id=new_movie.id))




# Initialize database with sample movies
# with app.app_context():
#     db.drop_all()   # deletes all tables
#     db.create_all() # recreates tables
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()
    
# initialize the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)