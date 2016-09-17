

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

#ouputFunc()

controid=os.fork()
if(controid==0):
    print "Control"
    controlDaemonFunct()
else:
    print "Inp"
    inpid=os.fork()
    if(inpid==0):
        inputDaemonFunc()
    else:
        print "Out"
        outid=os.fork()
        if(outid==0):
            ouputFunc()


while True:
    pass