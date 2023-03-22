from models.artist import Artist
from models.album import Album


import repositories.artist_repository as art_repo
import repositories.album_repository as album_repo

album_repo.delete_all()
art_repo.delete_all()

artist1 = Artist("Michael", "Jackson")
artist2 = Artist("Beyonce", "Knowles")
artist3 = Artist("Freddie", "Mercury")
artist4 = Artist("Elvis", "Presley")
artist5 = Artist("Jimi", "Hendrix")
artist6 = Artist("Prince", None)
artist7 = Artist("Adele", None)
artist8 = Artist("Bob", "Dylan")
artist9 = Artist("Stevie", "Wonder")
artist10 = Artist("Whitney", "Houston")

art_repo.save(artist1)
art_repo.save(artist2)
art_repo.save(artist3)
art_repo.save(artist4)
art_repo.save(artist5)
art_repo.save(artist6)
art_repo.save(artist7)
art_repo.save(artist8)
art_repo.save(artist9)
art_repo.save(artist10)

album1 = Album("Thriller", "Pop", 9, artist1)
album2 = Album("Bad", "Pop", 11, artist1)
album3 = Album("Off the Wall", "Pop", 10, artist1)
album4 = Album("Lemonade", "R&B", 12, artist2)
album5 = Album("Beyonce", "Pop", 14, artist2)
album6 = Album("I Am... Sasha Fierce", "Pop", 16, artist2)
album7 = Album("Mr. Bad Guy", "Pop", 11, artist3)
album8 = Album("Barcelona", "Classical Crossover", 8, artist3)
album9 = Album("The Great Pretender", "Pop", 14, artist3)
album10 = Album("Elvis Presley", "Rock and Roll", 12, artist4)
album11 = Album("From Elvis in Memphis", "Soul", 12, artist4)
album12 = Album("Elvis Country (I'm 10,000 Years Old)", "Country", 12, artist4)

album_repo.save(album1)
album_repo.save(album2)
album_repo.save(album3)
album_repo.save(album4)
album_repo.save(album5)
album_repo.save(album6)
album_repo.save(album7)
album_repo.save(album8)
album_repo.save(album9)
album_repo.save(album10)
album_repo.save(album11)
album_repo.save(album12)

selected_artist = art_repo.select(artist1.id)
print (f"The selected artists's name is: {selected_artist.first_name} {selected_artist.last_name}")

selected_album = album_repo.select(album2.id)
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

art_repo.delete(artist2.id)
album_repo.delete(album3.id)