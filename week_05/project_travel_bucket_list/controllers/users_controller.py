from flask import Flask, render_template, request, redirect, Blueprint
from models.user import User
import pdb

import repositories.continent_repository as continent_repo
import repositories.user_repository as user_repo
import repositories.city_repository as city_repo


users_blueprint = Blueprint("users", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@users_blueprint.route("/users")
def users():
    users = user_repo.select_all()
    # pdb.set_trace()
    return render_template("users/index.html", all_users = users)

@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html")

@users_blueprint.route("/users", methods=['POST'])
def create_user():
    username = request.form['username']
    user_fullname = request.form['name']
    user = User(username, user_fullname)
    user_repo.save(user)
    return redirect('/users')


@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
    selected_user = user_repo.select(id)
    return render_template("users/edit.html", user = selected_user)

@users_blueprint.route("/users/<id>", methods=['POST'])
def update_user(id):
    username = request.form['username']
    user_fullname = request.form['name']
    user = User(username, user_fullname, id)
    # pdb.set_trace()
    user_repo.update(user)
    return redirect('/users')

@users_blueprint.route("/users/<id>/delete", methods=['POST'])
def delete_user(id):
    user_repo.delete(id)
    return redirect('/users')