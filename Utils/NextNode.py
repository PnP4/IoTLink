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

