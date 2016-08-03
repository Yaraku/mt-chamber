import regex
import subprocess


class Command:
    InputSize = 1
    OutputSize = 1
    MultiThreadable = True
    ShareResources = False

    def __init__(self):
        return

    def routine(self, instream):
        travatar_result = instream[0]
        travatar_result = regex.sub(r"`\s", "`", travatar_result)
        travatar_result = regex.sub(r"\sn't", "n't", travatar_result)
        travatar_result = regex.sub(
            r"\s(\p{P})", r"\1", travatar_result
        )
        travatar_result = travatar_result.capitalize()
        travatar_result = regex.sub(
            r"^(\d*\W*\s+)(\w)",
            lambda m: m.group(1) + m.group(2).upper(),
            travatar_result
        )
        travatar_result = regex.sub(r"\bi\b", "I", travatar_result)
        symbol_set = r"[\p{N}\p{S}\p{P}--\p{Po}]"
        symbol_pattern = r"(?V1)({}+)\s+({}+)".format(symbol_set, symbol_set)
        while regex.search(symbol_pattern, travatar_result):
            travatar_result = regex.sub(
                symbol_pattern, r"\1\2", travatar_result
            )
        return (travatar_result,)
