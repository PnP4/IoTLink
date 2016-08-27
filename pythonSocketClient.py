import socket

clientsocket=socket.socket()

ConnetTo="127.0.0.1"
Port=8080;
BufferSize=1024

clientsocket.connect((ConnetTo,Port))
clientsocket.send("--------")
msg=clientsocket.recv(BufferSize)
print msg
clientsocket.close()