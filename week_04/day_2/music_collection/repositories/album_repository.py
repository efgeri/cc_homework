from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import pdb

def save(album):
    sql = "INSERT INTO albums (title, genre, tracks, artist_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.tracks, album.artist.id]
    
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album