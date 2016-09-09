import socket

from ConfigFile.ConfigParser import ConfigMonitor


class OutputDaemon:
    def __init__(self):
        self.cm = ConfigMonitor("/home/nrv/PycharmProjects/PnpGlobalLink/ConfigFile/config.xml")
        self.ip=self.cm.getOutputIP()
        self.port=self.cm.getOutputPort()

    def connect(self):
        try:
            self.clientsocket=socket.socket()
            self.clientsocket.connect((self.ip,self.port))
        except Exception as e:
            print "Error at output:- ",e
        
    def sendmsg(self):
        while True:
            msg="-------"
            msg = self.clientsocket.send(msg)
            if (not msg):
                break
            print msg
            fullmsg = fullmsg + msg
        self.clientsocket.close()


