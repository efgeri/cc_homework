import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1")
        self.song_pack_1 = [Song("Hotel California"), Song("Sweet Child O'Mine"), Song("Dancing Queen"), Song("I Will Always Love You"), Song("Heartbreak Hotel")]
        self.guest_1 = Guest("Michael Jackson")
        self.guest_2 = Guest("Mariah Carey")
        
    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room_1.name)

    def test_room_has_songs(self):
        self.room_1.song_list = self.song_pack_1
        self.assertEqual("Dancing Queen", self.room_1.song_list[2].name)

    def test_room_has_guests(self):
        self.room_1.guest_list = [self.guest_1, self.guest_2]
        self.assertEqual("Mariah Carey", self.room_1.guest_list[1].name)

    def test_can_remove_guests(self):
        self.room_1.guest_list = [self.guest_1, self.guest_2]
        self.room_1.guest_list.remove(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))