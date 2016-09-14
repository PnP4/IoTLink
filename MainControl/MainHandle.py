

import os
from ControlDeamonListen.DeamonListner import ControlDeamon

def controlDaemon():
    cont=ControlDeamon()
    if(cont.connect()):
        cont.handleClient()


controlDaemon()