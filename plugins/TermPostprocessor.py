import re


class Command:
    InputSize = 2
    OutputSize = 1
    MultiThreadable = True
    ShareResources = False

    def __init__(self):
        return

    def routine(self, instream):
        sentence = instream[0].rstrip()
        matched_terms = instream[1]
        for i, term in enumerate(matched_terms):
            sentence = sentence.replace('t{}'.format(i), term.text)
        return (sentence,)


class Term:
    def __init__(self, text: str):
        self.text = text


class MatchedTerm(Term):
    def __init__(self, text: str, position: int):
        Term.__init__(self, text)
        self.position = position

    def __repr__(self):
        return '{}: {}'.format(self.__class__, self.__str__())

    def __str__(self):
        return '{} @{}'.format(self.text, self.position)

