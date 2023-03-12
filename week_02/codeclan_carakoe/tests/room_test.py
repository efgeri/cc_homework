import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1", 3, 8)
        self.song_pack_1 = [Song("Hotel California"), Song("Sweet Child O'Mine"), Song("Dancing Queen"), Song("I Will Always Love You"), Song("Heartbreak Hotel")]
        self.guest_1 = Guest("Michael Jackson", 40)
        self.guest_2 = Guest("Mariah Carey", 7)
        self.guest_3 = Guest("Chris Martin", 30)
        self.guest_4 = Guest("Frank Sinatra", 25)
        self.guest_5 = Guest("Adele", 35)
        
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

    def test_room_can_charge(self):
        self.guest_1.decrease_wallet(self.room_1.entry_fee)
        self.assertEqual(32, self.guest_1.wallet)

    def test_not_enough_money(self):
        self.guest_2.decrease_wallet(self.room_1.entry_fee)
        self.assertEqual(7, self.guest_2.wallet)

    def test_too_many_people(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_4)
        self.room_1.check_in(self.guest_5)
        self.assertEqual(3, len(self.room_1.guest_list))
    