import random
import os
import time

import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(path)

from PnpLib import initPnp , pnpinput ,pnpprint




initPnp()

while True:
    for i in range(0, 150):

        print "send", str(i)
        #pnpinput(str(i));
        msg=pnpinput()
        print msg
        #time.sleep(1)


