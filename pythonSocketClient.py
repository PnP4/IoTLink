import socket

clientsocket=socket.socket()

ConnetTo="127.0.0.1"
Port=8080;
BufferSize=1024


clientsocket.connect((ConnetTo,Port))
clientsocket.send("--------")
fullmsg=""
while True:
    msg=clientsocket.recv(BufferSize)
    if (not msg):
        break
    print msg
    fullmsg=fullmsg+msg

print len(fullmsg)
clientsocket.close()