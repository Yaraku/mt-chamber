import re
import subprocess


class Command:

    InputSize = 1
    OutputSize = 2
    MultiThreadable = True
    ShareResources = False

    def __init__(self, travatar_path=None, config_path=None, showerr=False):
        if not travatar_path:
            travatar_path = "/usr/local/bin/travatar"
        if not config_path:
            config_path = "/vol/travatar_models/eijiro-added/travatar.ini"
        self.travatar = subprocess.Popen(
            [travatar_path, "-config_file", config_path, "-trace_out", "STDOUT",
             "-in_format", "penn", "-buffer", "false"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None if showerr else subprocess.PIPE,
            universal_newlines=True)
        self.span_reg = re.compile(r"\[([0-9]+), ([0-9]+)\]")

    def routine(self, instream):
        travatar_output = None
        travatar_trace = None
        try:
            penn_tree = instream[0]
            if penn_tree.startswith("failed\n"):
                return (penn_tree, "",)

            self.travatar.stdin.write(penn_tree)
            self.travatar.stdin.flush()

            travatar_trace = self.travatar.stdout.readline()
            spltrace = travatar_trace.split(" ||| ")

            m = self.span_reg.match(spltrace[1])

            inputlen = int(m.group(2))

            while True:
                travatar_trace_line = self.travatar.stdout.readline()
                spltrace = travatar_trace_line.split(" ||| ")
                spltree = spltrace[2].split(" ")
                for x in spltree:
                    if x and x[0] == x[-1] == "\"":
                        inputlen -= 1
                spltrace[4] = ".\n"
                travatar_trace += " ||| ".join(spltrace)
                if not inputlen:
                    break

            travatar_output = self.travatar.stdout.readline().rstrip("\n")
            return ("success\n" + travatar_output + "\n" + travatar_trace, travatar_output,)

        except:
            print('failed with {}\n{}\n{}'.format(instream[0], travatar_output, travatar_trace))

