from flask import Flask, render_template, request, redirect
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repo
import repositories.book_repository as book_repo


from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@books_blueprint.route("/books")
def books():
    books = book_repo.select_all() 
    return render_template("books/index.html", all_books = books)

@books_blueprint.route("/books/new")
def new_book():
    # get all the authors from the db
    all_authors = author_repo.select_all()
    # render the template
    return render_template("books/new.html", all_authors=all_authors)

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    year = request.form['year']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, genre, year, author)
    book_repo.save(book)
    return redirect('/books')

@books_blueprint.route("/books/<id>")
def show_book(id):
    selected_book = book_repo.select(id)
    return render_template("books/show.html", selected_book=selected_book)

@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repo.select(id)
    authors = author_repo.select_all()
    return render_template("books/edit.html", book=book, all_authors = authors)

@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    year = request.form['year']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, genre, year, author, id)
    book_repo.update(book)
    return redirect('/books')

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect('/books')
    

# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'