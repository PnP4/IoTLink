

import os
from ControlDeamonListen.DeamonListner import ControlDeamon
from inputDaemonListen.inpuDeamon import inputDaemon

def controlDaemonFunct():
    cont=ControlDeamon()
    if(cont.connect()):
        cont.handleClient()

def inputDaemonFunc():
    inpt=inputDaemon()
    if(inpt.connect()):
        inpt.handleClient()



#controlDaemonFunct()

inputDaemonFunc()