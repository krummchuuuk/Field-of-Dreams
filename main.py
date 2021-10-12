

class Word:
    def __init__(self, word: str) -> None:
        self.word = {}
        for letter in word:
            self.word[letter] = {
                "is_guest": False
            }
    
    def is_guest(self):
        values = []
        for let, v in self.word.items():
            values.append(v["is_guest"])

        return all(values)

    @property
    def letters(self):
        return self.word.keys()

    def guess_letter(self, letter):
        if letter in self.letters:
            for let in self.letters:
                if letter == let:
                    self.word[let]["is_guest"] = True
            return True
        
        return False

    def has_letter(self, letter) -> bool:
        if isinstance(letter, int):
            raise ValueError(f"<{letter}> is not a 'str' type")

        if letter.isdigit():
            raise ValueError(f"<{letter}> provided as 'str' type, but it's 'int' value")

        return letter in self.letters

class Game:
    pass


if __name__ == "__main__":
    pass