from nose.tools import assert_equals
from app.game import Game

def test_new_game():
    assert_equals(Game().score(), 0)
