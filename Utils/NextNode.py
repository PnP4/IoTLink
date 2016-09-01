import json
import socket
from socket import error as socket_error

class NextNode:
    def __init__(self,ipinp,ipport):
        self.ip=ipinp
        self.port=ipport

    def getport(self): #Retun the port of the current object
        try:
            return int(self.port)
        except:
            return None

    def getip(self):
        return self.ip

    def getConnectableObject(self):
        conlink=(self.getip(),self.getport())
        return conlink

    def checkStatus(self):
        clientsocket = socket.socket()
        clientsocket.connect(self.getConnectableObject())
        try:
            clientsocket = socket.socket()
            req_msg_json={}
            req_msg_json["type"]="checkstatus"
            clientsocket.sendall(json.dumps(req_msg_json))
        except socket_error as s_err:
            if(s_err.errno==111):
                return False   #ToDo add return message type



