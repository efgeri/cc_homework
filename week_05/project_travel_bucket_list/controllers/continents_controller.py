from flask import Flask, render_template, request, redirect
from models.continent import Continent
import pdb

import repositories.continent_repository as continent_repo
import repositories.user_repository as user_repo
import repositories.city_repository as city_repo


from flask import Blueprint

continents_blueprint = Blueprint("continents", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@continents_blueprint.route("/continents")
def continents():
    continents = continent_repo.select_all()
    # pdb.set_trace()
    return render_template("continents/index.html", all_continents = continents)

@continents_blueprint.route("/continents/new")
def new_continent():
    return render_template("continents/new.html")

@continents_blueprint.route("/continents", methods=['POST'])
def create_continent():
    continent_name = request.form['name']
    continent = Continent(continent_name)
    continent_repo.save(continent)
    return redirect('/continents')


@continents_blueprint.route("/continents/<id>/edit")
def edit_continent(id):
    continent = continent_repo.select(id)
    users = user_repo.select_all()
    cities = city_repo.select_all()
    return render_template("continents/edit.html", continent = continent, all_users = users, all_cities = cities)

@continents_blueprint.route("/continents/<id>", methods=['POST'])
def update_continent(id):
    user_id = request.form['user_id']
    city_id = request.form['city_id']
    user = user_repo.select(user_id)
    city = city_repo.select(city_id)
    continent = continent(user, city, id)
    # pdb.set_trace()
    continent_repo.update(continent)
    return redirect('/continents')

@continents_blueprint.route("/continents/<id>/delete", methods=['POST'])
def delete_continent(id):
    continent_repo.delete(id)
    return redirect('/continents')