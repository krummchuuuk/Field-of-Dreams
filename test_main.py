import unittest

from main import Game, Word

class TestWord(unittest.TestCase):
    def setUp(self) -> None:
        self.word = Word()


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()