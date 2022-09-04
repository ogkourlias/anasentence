#!/usr/bin/env python3

"""
    usage:
        python3 main.py [path to text file] or [plain text]
"""

# METADATA VARIABLES
__author__ = "Orfeas Gkourlias"
__status__ = "WIP"
__version__ = "0.1"

# IMPORTS
import sys
from english_words import english_words_set
english_words_set = list(english_words_set)

# CLASSES
class ana_sent():
    """ Creates the string object out of the input text. """
    def __init__(self, raw):
        self.original = raw

    def __str__(self):
        return self.original

    def sep(self):
        """ Seperates text by words and puts them into a list. """
        self.words = self.original.split()

    def find(self):
        """ Find anagrams for every word in the list and puts them into a dictionary. """
        self.ana_dict = {}
        for original in self.words:
            anagrams = []
            for other in english_words_set:
                if sorted(original.lower()) == sorted(other.lower()):
                    anagrams.append(other)
            self.ana_dict[original] = anagrams


        print(self.ana_dict)




# FUNCTIONS
def detect(raw):
    """ Detect whether input is a file or terminal string. """
    if ".txt" in raw:
        with open(raw, "r") as filehandle:
            text = ana_sent(filehandle.read())
    else:
        text = ana_sent(raw)
    return text


# MAIN
def main(args):
    """ Main function """
    text = detect(args[1])
    text.sep()
    text.find()
    # FINISH
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
