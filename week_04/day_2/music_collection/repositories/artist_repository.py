from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist(result['first_name'], result['last_name'], result['id'])
    return artist

def select_all():
    # setup an empty list to be returned
    artists = []
    # create a string of SQL
    sql = "SELECT * FROM artists"
    # send my SQL to run_sql
    results = run_sql(sql)
    # translate dictionaries into objects
    for row in results:
        artist = Artist(row['first_name'], row['last_name'], row['id'])
        artists.append(artist)
    # return the list
    return artists

def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE  FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)
