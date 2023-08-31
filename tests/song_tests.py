import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Jungle is massive", "General Levy")
    
    
    def test_song_has_name(self):
        self.assertEqual("Jungle is massive", self.song_1.name)

    def test_song_has_artist(self):
        self.assertEqual("General Levy", self.song_1.artist)
        