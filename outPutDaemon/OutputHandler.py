import os
import sys


class outputHandler:
    def __init__(self):
        self.path="/tmp/outFifo"

    def makeFifo(self):
        try:
            os.mkfifo(self.path)
            return True
        except Exception as e:
            print e
            return False

    def getmsg(self):
        outpipe = open(self.path, "r")
        msg=outpipe.read()
        outpipe.close()
        return msg
