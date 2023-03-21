from models.artist import Artist
from models.album import Album

import repositories.artist_repository as art_repo

artist1 = Artist("Ferenc", "Liszt")
art_repo.save(artist1)