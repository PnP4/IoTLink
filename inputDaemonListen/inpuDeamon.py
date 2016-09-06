import socket
from inputDaemonHandler import inputDaemonHandle
from ConfigFile.ConfigParser import ConfigMonitor


class inputDaemon:
    def __init__(self):
        self.cm = ConfigMonitor("/home/nrv/PycharmProjects/PnpGlobalLink/ConfigFile/config.xml")
        self.ip=''
        self.port=self.cm.getInputDaemonPort()
        self.bufferSize=1024
        self.handle=None

    def connect(self): #Bind the Socket
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serversocket.bind((self.ip, int(self.port)))
            self.serversocket.listen(1)
            self.handle=inputDaemonHandle()
            return True
        except Exception as e:
            print e, "InputDaemon @connect()"
            return False

    def handleClient(self):
        while True:
            clientsock, clientaddr = self.serversocket.accept()
            while True:  # Will read the pipe untill no of { and no of } matches. [Parserble]
                msg = clientsock.recv(self.bufferSize)
                self.handle.writeData(msg)
                print msg
            clientsock.close()

