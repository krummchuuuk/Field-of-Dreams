

class Word:
    def __init__(self, word: str) -> None:
        self.word = word

    def has_letter(self, letter) -> bool:
        if isinstance(letter, int):
            raise ValueError(f"<{letter}> is not a 'str' type")

        if letter.isdigit():
            raise ValueError(f"<{letter}> provided as 'str' type, but it's 'int' value")

        return letter in self.word

class Game:
    pass


if __name__ == "__main__":
    pass