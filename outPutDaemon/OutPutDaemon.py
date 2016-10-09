import os
import socket

import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(path)


from ConfigFile.ConfigParser import ConfigMonitor
from OutputHandler import outputHandler
from DB.DataBase import SQLDB
class OutputDaemon:
    def __init__(self):
        self.db = SQLDB()
        self.ip=self.db.getOutputDaemonIP()
        self.port=self.db.getOutputDaemonPort()

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


