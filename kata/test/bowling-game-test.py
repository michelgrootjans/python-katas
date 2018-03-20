from nose.tools import assert_equals
from app.game import Game

import unittest


class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_new_game(self):
        assert_equals(self.game.score(), 0)