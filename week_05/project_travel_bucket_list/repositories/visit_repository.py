from db.run_sql import run_sql

from models.visit import Visit
from models.city import City
from models.user import User
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

def save(visit):
    sql = "INSERT INTO visits ( user_id, city_id ) VALUES ( %s, %s ) RETURNING id"
    values = [visit.user.id, visit.city.id]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit


def select_all():
    visits = []

    sql = "SELECT * FROM visits"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        city = city_repository.select(row['city_id'])
        visit = Visit(user, city, row['id'])
        visits.append(visit)
    return visits


def city(visit):
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [visit.city.id]
    country = country_repository.select(visit.city.country.id)
    results = run_sql(sql, values)[0]
    city = City(results['name'], results['visit_date'], results['visited'], country, results['id'])
    return city


def user(visit):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [visit.user.id]
    results = run_sql(sql, values)[0]
    user = User(results['username'], results['name'], results['id'] )
    return user

def update(visit):
    sql = "UPDATE visits SET ( user_id, city_id ) = (%s, %s) WHERE id = %s"
    values = [visit.user.id, visit.city.id, visit.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM visits"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)
