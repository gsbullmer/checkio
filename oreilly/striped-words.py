import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    """
    Returns the number of "striped" words (alternating vowels and consonants)
    in `text`.
    """
    words = re.split(r"\W+", text)
    counter = 0

    def is_striped(word):
        """
        Return if the word consists of alternating vowels and consonants.
        """
        last_char = None
        for char in word:
            if last_char is (char in VOWELS):
                return False
            last_char = char in VOWELS
        return True

    for word in words:
        if len(word) > 1 and word.isalpha():
            counter += 1 if is_striped(word.upper()) else 0

    return counter

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
