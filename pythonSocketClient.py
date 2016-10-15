import json
import socket

clientsocket=socket.socket()

ConnetTo="192.168.1.7"
Port=8100;
BufferSize=1024
data={}
data["seq"]=[{"seqno":1,"name":"a"},{"seqno":2,"name":"b"},{"seqno":3,"name":"c"}]
data["you"]="a"
data["a"]=[{"ip":"192.168.1.7","conport":8100,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090}]
data["b"]=[{"ip":"192.168.1.20","conport":8100,"avialable":0,"inport":8090},{"ip":"192.168.1.8","conport":8100,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090}]
data["c"]=[{"ip":"127.0.0.1","conport":8100,"avialable":0,"inport":8090},{"ip":"192.168.1.2","conport":8100,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090}]


msg=json.dumps(data)
{"ip":"192.168.1.2","conport":8100,"avialable":0,"inport":8090}


clientsocket.connect((ConnetTo,Port))

fullmsg=""
#while True:
clientsocket.sendall(msg)
print clientsocket.recv(2048)

#print len(fullmsg)
clientsocket.close()