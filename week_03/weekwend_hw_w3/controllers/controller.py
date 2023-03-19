from flask import redirect, request, render_template

from app import app
from models.book import Book
from models.book_list import book_list, add_book, delete_book


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books_index():
    return render_template("books/index.html", books=book_list)


@app.route("/books/<index>")
def books_show(index):
    book = book_list[int(index)]
    return render_template("books/show.html", book=book, index=index)


@app.route("/books", methods=["POST"])
def books_create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre, False)
    add_book(new_book)
    return redirect("/books")


@app.route("/books/new")
def books_new():
    return render_template("books/new.html")


@app.route("/books/delete/<index>")
def books_delete(index):
    delete_book(int(index))
    return redirect("/books")


@app.route("/books/<index>", methods=["POST"])
def books_update(index):
    book = book_list[int(index)]
    if book.checked_out:
        if "checked_out" in request.form:
            checked_out = bool(request.form["checked_out"])
            book.toggle_check_in(checked_out)
        else:
            return redirect("/books/" + index)
    else:
        if "checked_out" in request.form:
            checked_out = bool(request.form["checked_out"])
            book.toggle_check_out(checked_out)
        else:
            return redirect("/books/" + index)

    return redirect("/books/" + index)


# Just a little note for the above route:
# Here's the code snippet originally posted for this route:

# @app.route("/books/<index>", methods=["POST"])
# def books_update(index):
#     book = books[int(index)]
#     checked_out = "checked_out" in request.form
#     book.toggle_check_out(checked_out)
#     return redirect("/books/" + index)

# Provided that the Pyhton method and the html side is written, this code will check out a book if the checkbox is checked,
# and check it back in if it's unchecked. My initial thought was to make the checkbox do the appropriate thing when checked
# (namely that if it's in, it should check it out and vice versa), and
# nothing if it's unchecked, since it's a more realistic use.
# I have misunderstood the above example code, I thought True or False value can actually be passed by the
# HTML form. In reality, this example above checks, if ANY checked_out value were passed on, and triggers the book class method for checking in.
# This took me a while to realise unfortunately, but when I did, I wanted to make a point that it's possible to do what I originally wanted.
# The resulting code is a bit hard to read, and it's possibly not the best implementation, I imagine there are better ways of doing this.
