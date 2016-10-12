import json
import os
import socket

import time

import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(path)

from DB.DataBase import SQLDB
import netifaces
from ControlMessageHandler import MessageHandle

class ControlDeamon:
    def __init__(self):  #At initilasisation phase it will read the config and config itself
        self.db = SQLDB()
        self.ListenIP = ''
        self.ListenPORT = int(self.db.getControlDaemonPort())
        self.BufferSize = 1024
        self.myips = self.getAllInterfaceAddresses() #This will be keep all his ips.


    def getAllInterfaceAddresses(self):  # get the idea of the network address of the node has.
        iplist=[]
        interface_list = netifaces.interfaces()
        for iname in interface_list:
            if (("eth" in iname) or ("wlan" in iname)): #get only eth and wlan (ethernet and wifi addresses)
                try:
                    internetIps = netifaces.ifaddresses(iname)[netifaces.AF_INET]  #fetch only IPv4 address only
                    iplist.append(internetIps[0]["addr"])
                except:
                    pass
        return iplist

    def filetrOutSelfIps(self,node):

        if(node.getip() in self.myips):
            return True
        if("127.0." in node.getip()):
            return True
        return False

    def connect(self):
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serversocket.bind((self.ListenIP, self.ListenPORT))
            self.serversocket.listen(1)  # Currenly listen to one
            return True
        except Exception as e:
            print e,"DemonListner @connect()"
            return False

    def handleClient(self):
        reply="********"
        gofornode=False
        while True:
            clientsock, clientaddr = self.serversocket.accept()
            print "Connection establish with client:- ", clientaddr
            totalclientdata=""

            while True:  # Will read the pipe untill no of { and no of } matches. [Parserble]
                jsonmsg=None
                ctime = time.time()
                clientdata = clientsock.recv(self.BufferSize)
                totalclientdata=totalclientdata+clientdata
                ctimenow = time.time()
                if(ctimenow==ctime):
                    break
                ctime=ctimenow
                try:
                    jsonmsg=json.loads(totalclientdata)  #Json is parsable means json is ccompletely receved
                    gofornode=True
                    break
                except Exception as e:
                    print e," while capturing the json commnd string ",


            print "\n",totalclientdata
            if(gofornode):#ToDO check the status and return I cant message
                handle=MessageHandle()
                nextList=handle.getNextNodes(jsonmsg)
                if(nextList!=None):
                    for node in nextList: #check all nodes sequentially for the availability
                        if(not self.filetrOutSelfIps(node)):
                            print "Done"
                            jsonmsg["you"]=handle.findNext(jsonmsg,jsonmsg["you"])["name"]
                            msg=self.conectToNextNode(node,jsonmsg)#This means the node is available
                            if(msg):
                                print "====="
                            else:
                                print "------"

                        else:
                            print "Loop detected"
                    clientsock.send(reply)
                    print len(reply)
                else:#ToDo CHECK THE PROGRAM AVAILABILITY  NEED TO GET THE PROGRAM NAME FROM THE MESSAGE
                    if(self.db.getStatus()=="available"):
                        reply={}
                        reply["msg"]="Done"
                        clientsock.send(json.dumps(reply))
                    else:
                        reply = {}
                        reply["msg"] = "Fail"
                        clientsock.send(json.dumps(reply))
                    #pass
            clientsock.close()

    def conectToNextNode(self,NextNode,msg):
        try:
            return NextNode.checkStatus(msg)

        except:
            return False


p=ControlDeamon()
if(p.connect()):
    p.handleClient()