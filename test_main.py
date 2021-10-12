import unittest

from main import Game, Word

class TestWord(unittest.TestCase):
    def setUp(self) -> None:
        word = "bread"
        self.word = Word(word)

    def test_try_to_guess_letter(self):
        self.assertEqual(self.word.guess_letter("r"), True)
        self.assertEqual(self.word.guess_letter("g"), False)

    def test_word_has_provided_letter(self):
        self.assertEqual(self.word.has_letter("r"), True)
        self.assertEqual(self.word.has_letter("j"), False)

    def test_that_word_is_guest(self):
        self.assertEqual(self.word.is_guest(), False)
        self.word.guess_letter("b")
        self.word.guess_letter("r")
        self.word.guess_letter("e")
        self.word.guess_letter("a")
        self.word.guess_letter("d")
        self.assertEqual(self.word.is_guest(), True)

class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()


if __name__ == "__main__":
    unittest.main()