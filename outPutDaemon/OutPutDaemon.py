import socket

class OutputDaemon:
    def __init__(self):
        self.ip='127.0.0.1'
        self.port=8080

    def connect(self):
        self.clientsocket=socket.socket()
        self.clientsocket.connect((self.ip,self.port))

    def sendmsg(self):
        while True:
            msg="-------"
            msg = self.clientsocket.send(msg)
            if (not msg):
                break
            print msg
            fullmsg = fullmsg + msg
        self.clientsocket.close()


