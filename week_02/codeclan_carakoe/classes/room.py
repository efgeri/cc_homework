class Room:
    def __init__(self, name, max_people, entry_fee):
        self.name = name
        self.song_list = []
        self.guest_list = []
        self.max_people = max_people
        self.entry_fee = entry_fee

    def check_in(self, guest):
        if len(self.guest_list) < self.max_people:
            self.guest_list.append(guest)
