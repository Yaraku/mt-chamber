import re


def kytea_escape(char):
    return '\{}'.format(char) if char in ['-', ' ', '|', '\\'] else char


class Command:
    InputSize = 1
    OutputSize = 2
    MultiThreadable = True
    ShareResources = False

    def __init__(self):
        return

    def routine(self, instream):
        matched_terms = []
        sentence = instream[0].rstrip('\n')
        for m in re.finditer(
            r'<span class="dict-\d+">(?!</span>).+?</span>',
            sentence
        ):
            matched_terms.append(MatchedTerm(m.group(0), m.start()))

        chunks = []
        matched_terms.sort(key=lambda x: x.position)
        offset = 0
        for i, term in enumerate(matched_terms):
            left = sentence[offset:term.position]
            if left:
                left = ' '.join([kytea_escape(x) for x in list(left)])
                chunks.append(left)
            replaced_term = 't{}'.format(i)
            annotated_term = '-'.join([
                kytea_escape(x) for x in list(replaced_term)
            ])
            chunks.append(annotated_term)
            offset = term.position + len(term.text)

        if offset < len(sentence):
            right = sentence[offset:]
            right = ' '.join([kytea_escape(x) for x in list(right)])
            chunks.append(right)
        annotated_sentence = '|'.join(chunks).strip('|- \n') + '\n'

        return (annotated_sentence, matched_terms)


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

