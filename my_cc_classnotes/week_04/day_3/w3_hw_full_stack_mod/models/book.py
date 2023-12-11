class Book:
    def __init__(self, title, author, genre, checked_out):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out

    def toggle_check_out(self, checked_out):
        if checked_out == True:
            self.checked_out = True

    def toggle_check_in(self, checked_out):
        if checked_out == True:
            self.checked_out = False
