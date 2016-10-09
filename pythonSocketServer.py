import socket



ListenIP='';
ListenPORT=8100;
BufferSize=1024

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serversocket.bind((ListenIP,ListenPORT))

serversocket.listen(1)  #Currenly listen to one

bigreply=""
for i in range(0,1000):
    bigreply=bigreply+str(i)+" "

while True:
    clientsock,clientaddr=serversocket.accept()
    print "Connection establish with client:- ", clientaddr

    while True:
        print "wait fro recv"
        clientdata=str(clientsock.recv(BufferSize))
        if(not clientdata):
            break
        #clientsock.send(bigreply);
        print clientdata
    clientsock.close()
print "Socket is created"