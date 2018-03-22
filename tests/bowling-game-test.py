from nose.tools import *
from app.bowling_game import *
import unittest

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_a_new_game(self):
        assert_equals(self.game.score(), 0)
