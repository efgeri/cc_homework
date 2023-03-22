from models.artist import Artist
from models.album import Album


import repositories.artist_repository as art_repo
import repositories.album_repository as album_repo

album_repo.delete_all()
art_repo.delete_all()

artist1 = Artist("Ferenc", "Liszt")
art_repo.save(artist1)
artist2 = Artist("Taylor", "Swift")
art_repo.save(artist2)

album1 = Album("Hungarian Rhapsody", "Classical", 19, artist1)
album_repo.save(album1)

selected_artist = art_repo.select(1)
print (f"The selected artists's name is: {selected_artist.first_name} {selected_artist.last_name}")

selected_album = album_repo.select(1)
print(f"The album title is:{selected_album.title}, which is {selected_album.genre} genre, has {selected_album.tracks} tracks on it, artist no.:{selected_album.artist.id}")

artist_list = art_repo.select_all()
for artist in artist_list:
    print(f"The artists's name is: {artist.first_name} {artist.last_name}")