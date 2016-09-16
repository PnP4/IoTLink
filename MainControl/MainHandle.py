

import os

import time

from ControlDeamonListen.DeamonListner import ControlDeamon
from inputDaemonListen.inpuDeamon import inputDaemon
from outPutDaemon.OutPutDaemon import OutputDaemon

def controlDaemonFunct():
    cont=ControlDeamon()
    if(cont.connect()):
        cont.handleClient()

def inputDaemonFunc():
    inpt=inputDaemon()
    if(inpt.connect()):
        inpt.handleClient()

def ouputFunc():
    outp=OutputDaemon()
    while(True):
        if(outp.connect()):
            break
        time.sleep(2)

    outp.sendmsg()



#controlDaemonFunct()

#inputDaemonFunc()

ouputFunc()