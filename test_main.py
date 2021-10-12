import unittest

from main import Game, Word

class TestWord(unittest.TestCase):
    def setUp(self) -> None:
        word = "bread"
        self.word = Word(word)

    def test_word_has_provided_letter(self):
        self.assertEqual(self.word.has_letter("r"), True)
        self.assertEqual(self.word.has_letter("j"), False)

class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()


if __name__ == "__main__":
    unittest.main()