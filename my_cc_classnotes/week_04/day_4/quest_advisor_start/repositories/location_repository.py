from db.run_sql import run_sql
from models.location import Location
from models.user import User

def save(location):
    sql = "INSERT INTO locations(name, category) VALUES ( %s, %s ) RETURNING id"
    values = [location.name, location.category]
    results = run_sql( sql, values )
    location.id = results[0]['id']
    return location


def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row['name'], row['category'], row['id'])
        locations.append(location)
    return locations


def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = Location(result['name'], result['category'], result['id'] )
    return location


def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)

def users(location):
    sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE location_id = %s"
    values = [location.id]
    results = run_sql(sql, values)
    users = []

    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users
