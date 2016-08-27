import socket



ListenIP='';
ListenPORT=8080;
BufferSize=1024

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serversocket.bind((ListenIP,ListenPORT))

serversocket.listen(1)  #Currenly listen to one

while True:
    clientsock,clientaddr=serversocket.accept()
    print "Connection establish with client:- ", clientaddr

    while True:
        clientdata=clientsock.recv(BufferSize)
        if(not clientsock):
            break
        clientsock.send("My response");
    clientsock.close()
print "Socket is created"