import socket

from ConfigFile.ConfigParser import ConfigMonitor
from OutputHandler import outputHandler

class OutputDaemon:
    def __init__(self):
        self.cm = ConfigMonitor("/home/nrv/PycharmProjects/PnpGlobalLink/ConfigFile/config.xml")
        self.ip=self.cm.getOutputIP()
        self.port=self.cm.getOutputPort()

    def connect(self):
        try:
            self.clientsocket=socket.socket()
            self.clientsocket.connect((self.ip,int(self.port)))
            self.handle=outputHandler()
            return True
        except Exception as e:
            print "Error at output:- ",e
            return False

    def sendmsg(self):
        while True:
            try:
                msg=self.handle.getmsg()
                self.clientsocket.send(msg)
            except Exception as e:
                print "Outputdaemn ",e
                break
        self.clientsocket.close()


