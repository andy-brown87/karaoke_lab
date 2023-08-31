import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Harry")
        self.room_1 = Room("Jungle Room", [self.guest])
        
    
    
    def test_room_has_name(self):
        self.assertEqual("Jungle Room", self.room_1.name)

    def test_room_has_singers(self):
        self.assertEqual("Harry", self.guest.name)
        

    