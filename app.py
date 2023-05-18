from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import cv2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviedb.db'
db = SQLAlchemy(app)

# Model for the movies table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    poster = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    actors = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    gif_url = db.Column(db.String(255))

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Get all the movies from the database
    movies = Movie.query.all()

    return render_template('index.html.jinja2', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    # Get the movie from the database
    movie = Movie.query.get(movie_id)

    return render_template('movie.html.jinja2', movie=movie)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the data from the form
    file = request.files['poster']
    title = request.form['title']
    description = request.form['description']
    year = request.form['year']
    actors = request.form['actors']
    director = request.form['director']
    gif_url = request.form['gif_url']

    # Save the image to the static/images folder
    filename = file.filename
    file.save(os.path.join('static/images', filename))

    # Create a new movie object and save it to the database
    movie = Movie(title=title, poster=filename, description=description, year=year, actors=actors, director=director, gif_url=gif_url)
    db.session.add(movie)
    db.session.commit()

    return "Success", 201

@app.route('/movie/<int:movie_id>/delete', methods=['POST'])
def delete(movie_id):
    # Get the movie from the database
    movie = Movie.query.get(movie_id)

    # Delete the movie from the database
    db.session.delete(movie)
    db.session.commit()

    return "Success", 201

@app.route('/detect_faces/<int:movie_id>')
def detect_faces(movie_id):
    # Get the movie from the database
    movie = Movie.query.get(movie_id)

    # Load the image from the static/images folder
    image_path = os.path.join('static/images', movie.poster)

    # Load the image and convert it to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    return render_template('movie.html.jinja2', movie=movie, faces=faces)

if __name__ == '__main__':
    app.run(debug=True)
