from models.artist import Artist
from models.album import Album

import repositories.artist_repository as art_repo
import repositories.album_repository as album_repo

album_repo.delete_all()
art_repo.delete_all()

artist1 = Artist("Ferenc", "Liszt")
art_repo.save(artist1)

album1 = Album("Hungarian Rhapsody", "Classical", 19, artist1)
album_repo.save(album1)