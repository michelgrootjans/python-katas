from nose.tools import *
from app.bowling_game import *
import unittest

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_a_new_game(self):
        assert_equals(self.game.score(), 0)

    def test_rolling_0(self):
        self.game.roll(0)
        assert_equals(self.game.score(), 0)

    def test_rolling_1(self):
        self.game.roll(1)
        assert_equals(self.game.score(), 1)

    def test_rolling_1_1(self):
        self.game.roll(1)
        self.game.roll(1)
        assert_equals(self.game.score(), 2)

    def test_rolling_2(self):
        self.game.roll(2)
        assert_equals(self.game.score(), 2)

    def test_rolling_all_1(self):
        for i in range(0,20):
            self.game.roll(1)
        assert_equals(self.game.score(), 20)

    def test_spare_1(self):
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(1)
        assert_equals(self.game.score(), 12)

    def test_spare(self):
        self.game.roll(4)
        self.game.roll(6)
        assert_equals(self.game.score(), 10)

    def test_spare_spare_1(self):
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(1)
        assert_equals(self.game.score(), (4+6+4) + (4+6+1) + 1)

    def test_all_5es(self):
        for _ in range(0,21):
            self.game.roll(5)
        assert_equals(self.game.score(), 15*10)

    def test_strike_1_2(self):
        self.game.roll(10)
        self.game.roll(1)
        self.game.roll(2)
        assert_equals(self.game.score(), (10+1+2) + (1+2))

    def test_strike_strike_1_2(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(1)
        self.game.roll(2)
        assert_equals(self.game.score(), (10+10+1) + (10+1+2) + (1+2))

    def test_a_perfect_game(self):
        for _ in range(0,12):
            self.game.roll(10)
        assert_equals(self.game.score(), 300)







