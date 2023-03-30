from flask import Flask, render_template, request, redirect
from models.visit import Visit
from models.continent import Continent
from models.country import Country
from models.city import City
from models.user import User

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
    visits = []
    all_entries = visit_repo.select_by_user(id)
    for entry in all_entries:
        if entry.visited == True:
            visits.append(entry)
    return render_template("user_visits/index.html", user = selected_user, all_visits = visits)

@user_visits_blueprint.route("/users/<id>/wishlist")
def user_wishlist(id):
    selected_user = user_repo.select(id)
    wishlist = []
    all_entries = visit_repo.select_by_user(id)
    for entry in all_entries:
        if entry.visited == False:
            wishlist.append(entry)
    return render_template("user_visits/wishlist.html", user = selected_user, wishlist = wishlist)

# 1
@user_visits_blueprint.route("/users/<id>/visits/new")
def user_new_visit(id):
    all_countries = country_repo.select_all()
    for country in all_countries:
        if country.name == "New country":
            country_repo.delete(country.id)
    all_cities = city_repo.select_all()
    for city in all_cities:
        if city.name == "New city":
            city_repo.delete(city.id)
    selected_user = user_repo.select(id)
    continents = continent_repo.select_all()
    return render_template("user_visits/new.html", user = selected_user, all_continents = continents)

# 2
@user_visits_blueprint.route("/users/<id>/visits", methods=['POST'])
def user_create_visit(id):
    continent_id = request.form['continent_id']
    user = user_repo.select(id)
    continent = continent_repo.select(continent_id)
    country = Country("New country", continent)
    country_repo.save(country)
    city = City("New city", country)
    city_repo.save(city)
    visit = Visit(user, city, False)
    visit_repo.save(visit)
    return user_edit_country(user.id, visit.id)

# 3
@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/countries")
def user_edit_country(user_id, visit_id):
    selected_visit = visit_repo.select(visit_id)
    selected_user = user_repo.select(user_id)
    selected_countries = country_repo.countries_by_continent(selected_visit.city.country.continent)
    return render_template ("user_visits/select_country.html", user = selected_user, visit = selected_visit, all_countries = selected_countries)

# 4
@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/countries/update", methods=['POST'])
def user_update_country(user_id, visit_id):
    visit = visit_repo.select(visit_id)
    country = country_repo.select(request.form['country_id'])
    visit.city.country = country
    city_repo.update(visit.city)       
    if country.name == "New country":
        return user_new_country(user_id, visit_id)
    return user_edit_city(user_id, visit_id)
# az utolso sor csak egy dummy, innen kell folytatni

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/countries", methods=['POST'])
def user_create_country(user_id, visit_id):
    visit = visit_repo.select(visit_id)
    # country = Country(request.form['country_name'], visit.city.country.continent)
    # country_repo.save(country)
    visit.city.country.name = request.form['country_name']
    country_repo.update(visit.city.country)
    return user_edit_city(user_id, visit_id)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/cities")
def user_edit_city(user_id, visit_id):
    selected_visit = visit_repo.select(visit_id)
    selected_user = user_repo.select(user_id)
    selected_cities = city_repo.cities_by_country(selected_visit.city.country)
    return render_template ("user_visits/select_city.html", user = selected_user, visit = selected_visit, all_cities = selected_cities)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/cities/update", methods=['POST'])
def user_update_city(user_id, visit_id):
    visit = visit_repo.select(visit_id)
    city = city_repo.select(request.form['city_id'])
    visit.city = city
    visit_repo.update(visit)
    if city.name == "New city":
        return user_new_city(user_id, visit_id)
    return user_edit_visit(user_id, visit_id)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/edit")
def user_edit_visit(user_id, visit_id):
    selected_visit = visit_repo.select(visit_id)
    selected_user = user_repo.select(user_id)
    selected_countries = country_repo.countries_by_continent(selected_visit.city.country.continent)
    selected_cities = city_repo.select_all()
    return render_template("user_visits/edit.html", visit = selected_visit, user = selected_user, all_cities = selected_cities, all_countries = selected_countries)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/countries/new")
def user_new_country(user_id, visit_id):
    user = user_repo.select(user_id)
    visit = visit_repo.select(visit_id)
    return render_template("user_visits/new_country.html", user = user, visit = visit)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>", methods=['POST'])
def user_update_visit(user_id, visit_id):
    city_id = request.form['city_id']
    country_id = request.form['country_id']
    date = request.form['visit_date']
    if date == "":
        date = None
    visited = request.form['visited']
    visit = visit_repo.select(visit_id)
    user = user_repo.select(user_id)
    country = country_repo.select(country_id)
    city = city_repo.select(city_id)
    if country.name == "New country":
        return user_new_country(user.id, visit.id)
    if city.name == "New city":
        return user_new_city(user.id, visit.id)
    visit = Visit(user, city, visited, date, visit_id)
    visit_repo.update(visit)
    return user_visits(user_id)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/cities", methods=['POST'])
def user_create_city(user_id, visit_id):
    # we probably don't need to pass the variables down here, i'll check later
    visit = visit_repo.select(visit_id)
    # city = City(request.form['city_name'], visit.city.country)
    # city_repo.save(city)
    visit.city.name = request.form['city_name']
    city_repo.update(visit.city)
    return user_edit_visit(user_id, visit_id)

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/cities/new")
def user_new_city(user_id, visit_id):
    user = user_repo.select(user_id)
    visit = visit_repo.select(visit_id)
    return render_template("user_visits/new_city.html", user = user, visit = visit)                   

@user_visits_blueprint.route("/users/<user_id>/visits/<visit_id>/delete", methods=['POST'])
def delete_visit(user_id, visit_id):
    visit_repo.delete(visit_id)
    return user_visits(user_id)


