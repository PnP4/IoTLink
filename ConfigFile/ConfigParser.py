import xml.etree.ElementTree as xparse

tree = xparse.parse('config.xml')
print tree

class ConfigMonitor:

    def __init__(self,filepath='config.xml'):
        self.config = xparse.parse(filepath)
        self.ip=self.config.getiterator("ip")[0]
        self.port = self.config.getiterator("port")[0]


    def getPort(self):
        return int(self.port)

    def getIp(self):
        return self.ip



configmonitor=ConfigMonitor()
configmonitor.getPort()