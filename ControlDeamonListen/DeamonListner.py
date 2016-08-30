import socket
from ConfigFile.ConfigParser import ConfigMonitor



cm=ConfigMonitor("/home/nrv/PycharmProjects/PnpGlobalLink/ConfigFile/config.xml")


ListenIP=cm.getIp();
ListenPORT=int(cm.getPort())
BufferSize=1024



serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serversocket.bind((ListenIP,ListenPORT))

serversocket.listen(1)  #Currenly listen to one

reply=" This Reply"

while True:
    clientsock,clientaddr=serversocket.accept()
    print "Connection establish with client:- ", clientaddr

    while True:
        clientdata=clientsock.recv(BufferSize)
        if(not clientsock):
            break
        clientsock.send(reply);
        print len(reply)
        clientsock.close()
