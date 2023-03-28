from flask import Flask, render_template, request, redirect
from models.visit import Visit
from models.continent import Continent
from models.country import Country
from models.city import City
from models.user import User
import pdb

import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo
import repositories.user_repository as user_repo
import repositories.visit_repository as visit_repo


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
    all_countries = country_repo.select_all()
    for country in all_countries:
        if country.name == "New country":
            country_repo.delete(country.id)
    selected_user = user_repo.select(id)
    continents = continent_repo.select_all()
    return render_template("user_visits/new.html", user = selected_user, all_continents = continents)

# @user_visits_blueprint.route("/users/<id>/continents")
# def user_select_continent(id):
#     all_continents = continent_repo.select_all()
#     selected_user = user_repo.select(id)
#     return render_template("select_continent.html", all_continents = all_continents, user = selected_user)



@user_visits_blueprint.route("/users/<id>/visits", methods=['POST'])
def user_create_visit(id):
    continent_id = request.form['continent_id']
    user = user_repo.select(id)
    continent = continent_repo.select(continent_id)
    country = Country("New country", continent)
    country_repo.save(country)
    city = City("New city", True, country)
    city_repo.save(city)
    visit = Visit(user, city)
    visit_repo.save(visit)
    return edit_visit(user.id, visit.id)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/edit")
def edit_visit(user_id, visit_id):
    selected_visit = visit_repo.select(visit_id)
    selected_user = user_repo.select(user_id)
    countries = country_repo.select_all()
    cities = city_repo.select_all()
    return render_template("user_visits/edit.html", visit = selected_visit, user = selected_user, all_cities = cities, all_countries = countries)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/countries/new")
def user_new_country(user_id, visit_id):
    user = user_repo.select(user_id)
    visit = visit_repo.select(visit_id)
    country = country_repo.select(visit.city.country.id)    
    return render_template("user_visits/new_country.html", user = user, visit = visit, country = country)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>", methods=['POST'])
def user_update_visit(user_id, visit_id):
    city_id = request.form['city_id']
    country_id = request.form['country_id']
    visit = visit_repo.select(visit_id)
    user = user_repo.select(user_id)
    country = country_repo.select(country_id)
    city = city_repo.select(city_id)
    if country.name == "New country":
        return user_new_country(user.id, visit.id)
    visit = Visit(user, city, visit_id)
    visit_repo.update(visit)
    return user_visits(user_id)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/cities/new")
def user_new_city(user_id, visit_id):
    user = user_repo.select(user_id)
    visit = visit_repo.select(visit_id)
    country = country_repo.select(visit.city.country.id) 
    return render_template("user_visits/new_city.html", user = user, visit = visit, country = country)                   


@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/countries", methods=['POST'])
def user_create_country(user_id, visit_id):
    visit = visit_repo.select(visit_id)
    country = country_repo.select(visit.city.country.id)
    country.name = request.form['country_name']
    country_repo.update(country)
    return user_new_city(user_id, visit_id)
# az utolso sor cssak egy dummy, innen kell folytatni


@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/delete", methods=['POST'])
def delete_visit(user_id, visit_id):
    visit_repo.delete(visit_id)
    return user_visits(user_id)
