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
                travatar_result = travatar_result.replace('-lrb- ', '(')
                travatar_result = travatar_result.replace(' -rrb-', ')')
                travatar_result = travatar_result.replace('-lsb- ', '[')
                travatar_result = travatar_result.replace(' -rsb-', ']')
                travatar_result = travatar_result.replace('-lcb- ', '{')
                travatar_result = travatar_result.replace(' -rcb-', '}')
                return (travatar_result,)

