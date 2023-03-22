from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as art_repo

def save(album):
    sql = "INSERT INTO albums (title, genre, tracks, artist_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.tracks, album.artist.id]
    
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = art_repo.select(result['artist_id'])
        album = Album(result['title'], result['genre'], result['tracks'], artist)
    return album