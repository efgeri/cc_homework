from db.run_sql import run_sql
import repositories.country_repository as country_repo
# import pdb

from models.city import City
from models.user import User

def save(city):
    sql = "INSERT INTO cities (name, visited, visit_date, country_id) VALUES ( %s, %s, %s, %s) RETURNING id"
    values = [city.name, city.visited, city.visit_date, city.country.id]
    results = run_sql( sql, values )
    # pdb.set_trace()
    city.id = results[0]['id']


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repo.select(row['country_id'])
        city = City(row['name'], row['visit_date'], row['visited'], country, row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repo.select(result['country_id'])
        city = City(result['name'], result['visit_date'], result['visited'], country, result['id'])
    return city

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def update(city):
    sql = "UPDATE cities SET (name, visit_date, visited, country_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.visit_date, city.visited, city.country.id, city.id]
    run_sql(sql, values)

def cities_by_country(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['visit_date'], row['visited'], country, row['id'])
        cities.append(city)
    return cities

def visited_by_user(city):
    users = []

    sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        user = User(row['username'], row['name'], row['id'] )
        users.append(user)

    return users
