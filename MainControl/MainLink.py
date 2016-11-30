import json
import os
import subprocess

import time

import sys



path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(path)

from ControlDeamonListen.DeamonListner import ControlDeamon
from inputDaemonListen.inpuDeamon import inputDaemon
from outPutDaemon.OutPutDaemon import OutputDaemon

def processCleanUp(procname):
    tmp = os.popen("ps aux").read()
    pslist=[]
    #print tmp
    for line in tmp.split("\n"):
        x=1
        line=line.strip()
        procdata=line.split(" ")
        for c in range(0,procdata.count('')):
            procdata.remove('')
        #print procdata
        try:
            if(procname in procdata[11]):
                try:
                    pslist.append(int(procdata[1]))
                except Exception as e:
                    pass
                    #print "Error occured in init process cleanup:- "+e.message
        except Exception as e:
            pass
            #print "Error occured in init process cleanup Main try :- "+e.message
    #print pslist
    for p in pslist:
        try:
            if(os.getpid()!=p):
                print p,os.getpid()
                os.kill(p,9)
        except Exception as e:
            print "Error occured in init process cleanup (Killing):- " + e.message



path = "/tmp/control"
try:
    os.mkfifo(path)
except Exception as e:
    pass
import os

processCleanUp("inputDeamon.py")
processCleanUp("outputdeamon.py")

dir_path = os.path.dirname(os.path.realpath(__file__))

proccontrol = subprocess.Popen(['python', dir_path+'/newDeamon.py'])
procinput = subprocess.Popen(['python', dir_path+'/inputdeamon/inputDeamon.py'])
procoutput = subprocess.Popen(['python', dir_path+'/outputdeamon/outputdeamon.py'])
process = subprocess.Popen(['python', os.environ['HOME']+"/a.py"])

def getFromControl():
    fifo = open(path, "r")
    msg=fifo.read()



while(1):

    settings=json.dumps(getFromControl())
    time.sleep(5)
    processCleanUp("inputDeamon.py")
    processCleanUp("outputdeamon.py")
    procinput.kill()
    procoutput.kill()
    procinput = subprocess.Popen(['python', dir_path + '/inputdeamon/inputDeamon.py'])
    procoutput = subprocess.Popen(['python', dir_path + '/outputdeamon/outputdeamon.py'])





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
    failcount=0;
    while(True):
        if(outp.connect()):
            print "Connected"
            outp.sendmsg()
        #break
        print "Error @ Output"
        failcount=failcount+1
        if(failcount>5):
            print "Next Down"
            #recoverNext()
            break
        time.sleep(2)



try:
    path = os.getenv("HOME") + "/MetaPnpGlobal"
    if not os.path.exists(path):
        print "---"
        os.makedirs(path)
except Exception as e:
    print e
filepath = path + "/config.json"
print filepath
try:
    confile=open(filepath,'r')
except Exception as e:
    print"at MainHandler"
    confile = open(filepath, 'w+')
    confile.close()
    confile = open(filepath, 'r')
msg=confile.read()
if(msg!=None):
    curmdh=md5(msg)
else:
    curmdh=None
confile.close()



#controlDaemonFunct()

#inputDaemonFunc()

#ouputFunc()

controid=os.fork()
if(controid==0):
    print "Control"
    controlDaemonFunct()
else:

    inpid=os.fork()
    if(inpid==0):
        print "Inp"
        inputDaemonFunc()
    else:

        outid=os.fork()
        if(outid==0):
            print "Out"
            ouputFunc()

        else:
            while True:
                confile = open(filepath)
                msg = confile.read()
                if (msg != None):
                    newmdh = md5(msg)
                else:
                    newmdh = None
                confile.close()
                if (curmdh != newmdh):
                    print "Got File Change"
                time.sleep(5)
