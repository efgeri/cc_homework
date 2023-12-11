from flask import render_template, redirect, request
from app import app
from models.movie import movies, Movie

@app.route('/movies')
def index():
    return render_template('movies/index.html', all_movies = movies)

@app.route("/movies", methods=["POST"])
def create():
    new_movie = Movie(request.form['title'], request.form['year'])
    movies.append(new_movie)
    return redirect("/movies")

@app.route("/movies/<id>/delete", methods=['POST'])
def delete_movies(id):
    movies.pop(int(id)-1)
    return redirect("/movies")