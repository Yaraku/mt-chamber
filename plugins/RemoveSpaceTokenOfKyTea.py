import subprocess


class Command:

        InputSize = 1
        OutputSize = 1
        MultiThreadable = True
        ShareResources = False

        def __init__(self):
                return

        def routine(self, instream):
                kytea_result = instream[0]
                clean_kytea_result = kytea_result.replace('\\ /補助記号', '')
                clean_kytea_result = clean_kytea_result.replace('  ', ' ').strip()
                return (clean_kytea_result + '\n',)

