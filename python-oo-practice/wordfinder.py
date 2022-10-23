"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        with open(path, mode='r') as file:
            self.words = file.readlines()
            print(f'{len(self.words)} words read')
    def test(self):
        return random.choice(self.words)

test = WordFinder('words.txt')
test.test()


class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)

    def findWord(self):
        word = random.choice(self.test())
        while word[0] == '#' or len(word) < 1:
            word = random.choice(self.test())
        return word
