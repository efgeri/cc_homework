from db.run_sql import run_sql
import repositories.country_repository as country_repository

from models.user import User
from models.city import City


def save(user):
    sql = "INSERT INTO users (username, name) VALUES ( %s, %s ) RETURNING id"
    values = [user.username, user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['username'], row['name'], row['id'])
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = User(result['username'], result['name'], result['id'] )
    return user

def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def visited_cities(id):
    cities = []

    sql = "SELECT cities.* FROM cities INNER JOIN visits ON visits.city_id = cities.id AND visits.visited = 'False' WHERE user_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['id'])
        cities.append(city)

    return cities

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def update(user):
    sql = "UPDATE users SET (username, name) = (%s, %s) WHERE id = %s"
    values = [user.username, user.name, user.id]
    run_sql(sql, values)