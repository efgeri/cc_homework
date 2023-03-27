from flask import Flask, render_template, request, redirect
from models.visit import Visit
import pdb

import repositories.visit_repository as visit_repo
import repositories.user_repository as user_repo
import repositories.city_repository as city_repo


from flask import Blueprint

user_visits_blueprint = Blueprint("user_visits", __name__)

# RESTful CRUD Routes

@user_visits_blueprint.route("/users")


@user_visits_blueprint.route("/users/<id>/visits")
def visits(id):
    visits = visit_repo.select_by_user(id)
    # pdb.set_trace()
    return render_template("visits/index.html", all_visits = visits)

@user_visits_blueprint.route("/visits/new")
def new_visit():
    users = user_repo.select_all()
    cities = city_repo.select_all()
    return render_template("visits/new.html", all_users = users, all_cities = cities)

@user_visits_blueprint.route("/visits", methods=['POST'])
def create_visit():
    user_id = request.form['user_id']
    city_id = request.form['city_id']
    user = user_repo.select(user_id)
    city = city_repo.select(city_id)
    visit = Visit(user, city)
    visit_repo.save(visit)
    return redirect('/visits')


@user_visits_blueprint.route("/visits/<id>/edit")
def edit_visit(id):
    visit = visit_repo.select(id)
    users = user_repo.select_all()
    cities = city_repo.select_all()
    return render_template("visits/edit.html", visit = visit, all_users = users, all_cities = cities)

@user_visits_blueprint.route("/visits/<id>", methods=['POST'])
def update_visit(id):
    user_id = request.form['user_id']
    city_id = request.form['city_id']
    user = user_repo.select(user_id)
    city = city_repo.select(city_id)
    visit = Visit(user, city, id)
    # pdb.set_trace()
    visit_repo.update(visit)
    return redirect('/visits')

@user_visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
def delete_visit(id):
    visit_repo.delete(id)
    return redirect('/visits')