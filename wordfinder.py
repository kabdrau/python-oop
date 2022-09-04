"""Word Finder: finds random words from a dictionary."""
from random import choice, randint

class WordFinder:
    """Machine for finding random words from text file.
    >>> w = WordFinder('words.txt')
    235888 words read

    >>> isinstance(w.random(), str)
    True
    """
    def __init__(self, path):
        """Read txt file and reports # words read."""
        self.words = self.open_file(path)
        print(f"{len(self.words)} words read")

    def open_file(self, file_path):
        """Open, read from txt file and return all items."""
        file = open(file_path)
        lst = [word[:-2] for word in file]
        file.close()
        return lst
    
    def random(self):
        """Return random word."""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Machine for finding random words from text file.
    >>> w = SpecialWordFinder('words.txt')
    235886 words read
    """
    def open_file(self, file_path):
        """Open, read from txt file and return all items, ignore #comments and ''empty strings."""
        file = open(file_path)
        lst = [word[:-2] for word in file if not word.startswith("#") and word.strip()]
        file.close()
        return lst