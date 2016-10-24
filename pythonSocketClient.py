import json
import socket

clientsocket=socket.socket()

ConnetTo="138.197.26.183"
Port=8100;
BufferSize=1024
data={}
data["seq"]=[{"seqno":1,"name":"a"},{"seqno":2,"name":"b"},{"seqno":3,"name":"c"},{"seqno":4,"name":"d"}]
data["you"]="a"
data["a"]=[{"ip":"192.168.1.70","conport":8100,"avialable":0,"inport":8090},{"ip":"138.197.26.183","conport":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090}]
data["b"]=[{"ip":"192.168.1.20","conport":8100,"avialable":0,"inport":8090},{"ip":"138.197.30.34","conport":8100,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090}]
data["c"]=[{"ip":"127.0.0.1","conport":8100,"avialable":0,"inport":8090},{"ip":"138.197.8.95","conport":8100,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090}]
data["d"]=[{"ip":"127.0.0.1","conport":8100,"avialable":0,"inport":8090},{"ip":"192.34.63.88","conport":8100,"avialable":0,"inport":8090},{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090}]
data["prgid"]="125899"
data["msgtype"]="link"


msg=json.dumps(data)
{"ip":"192.168.1.2","conport":8100,"avialable":0,"inport":8090}


clientsocket.connect((ConnetTo,Port))

fullmsg=""
#while True:
clientsocket.sendall(msg)
print clientsocket.recv(2048)

#print len(fullmsg)
clientsocket.close()