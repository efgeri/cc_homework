from flask import Flask, render_template, request, redirect
from models.visit import Visit
import pdb

import repositories.visit_repository as visit_repo
import repositories.user_repository as user_repo
import repositories.city_repository as city_repo


from flask import Blueprint

user_visits_blueprint = Blueprint("user_visits", __name__)

# RESTful CRUD Routes  

@user_visits_blueprint.route("/users/<id>/visits")
def user_visits(id):
    selected_user = user_repo.select(id)
    visits = visit_repo.select_by_user(id)
    return render_template("user_visits/index.html", user = selected_user, all_visits = visits)

@user_visits_blueprint.route("/users/<id>/visits/new")
def user_new_visit(id):
    selected_user = user_repo.select(id)
    cities = city_repo.select_all()
    return render_template("user_visits/new.html", user = selected_user, all_cities = cities)

@user_visits_blueprint.route("/users/<id>/visits", methods=['POST'])
def user_create_visit(id):
    city_id = request.form['city_id']
    user = user_repo.select(id)
    city = city_repo.select(city_id)
    visit = Visit(user, city)
    visit_repo.save(visit)
    return user_visits(id)


@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/edit")
def edit_visit(user_id, visit_id):
    selected_visit = visit_repo.select(visit_id)
    selected_user = user_repo.select(user_id)
    cities = city_repo.select_all()
    return render_template("user_visits/edit.html", visit = selected_visit, user = selected_user, all_cities = cities)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>", methods=['POST'])
def user_update_visit(user_id, visit_id):
    city_id = request.form['city_id']
    user = user_repo.select(user_id)
    city = city_repo.select(city_id)
    visit = Visit(user, city, visit_id)
    visit_repo.update(visit)
    return user_visits(user_id)

@user_visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
def delete_visit(id):
    visit_repo.delete(id)
    return redirect('/visits')