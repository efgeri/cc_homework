class Album:
    
    def __init__(self, title, genre, tracks, artist, id = None):
        self.title = title
        self.genre = genre
        self.tracks = tracks
        self.artist = artist
        self.id = id