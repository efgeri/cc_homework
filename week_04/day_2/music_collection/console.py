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
album2 = Album("Midnights", "Pop", 13, artist2)
album_repo.save(album2)
album3 = Album("evermore", "Pop", 15, artist2)
album_repo.save(album3)

selected_artist = art_repo.select(1)
print (f"The selected artists's name is: {selected_artist.first_name} {selected_artist.last_name}")

selected_album = album_repo.select(1)
print(f"The selected album title is:{selected_album.title}, which is {selected_album.genre} genre, has {selected_album.tracks} tracks on it, artist no.:{selected_album.artist.id}")

artist_list = art_repo.select_all()
for artist in artist_list:
    print(f"The artists's name is: {artist.first_name} {artist.last_name}")

album_list = album_repo.select_all()
for album in album_list:
    print(f"The album title is:{album.title}, which is {album.genre} genre, has {album.tracks} tracks on it, artist no.:{album.artist.id}")

taylor_albums = album_repo.album_by_artist(artist2)
for album in taylor_albums:
    print(f"{album.artist.first_name} has {len(taylor_albums)} albums. The album title is: {album.title}, which is {album.genre} genre, has {album.tracks} tracks on it, artist no.:{album.artist.id}")

artist2.first_name = "Taylorino"
artist2.last_name = "Swift"
art_repo.update(artist2)

album2.title = "Daylights"
album_repo.update(album2)