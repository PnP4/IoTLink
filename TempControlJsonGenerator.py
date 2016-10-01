"a|b|c"
import json

#name will be program name

data={}
data["seq"]=[{"seqno":1,"name":"a"},{"seqno":2,"name":"b"},{"seqno":3,"name":"c"},{"seqno":4,"name":"d"}]
data["you"]="b"
data["a"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]
data["b"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]
data["c"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]
data["d"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]

print json.dumps(data)

msg=json.dumps(data)


recveddemo=json.loads(msg)

myprogram=recveddemo["you"]

def findNext(fulljson,myprogram):
    sequence=fulljson["seq"]
    myseqno=-1
    for i in sequence:
        if(i["name"]==myprogram):
            myseqno=i["seqno"]
            break
    if(myseqno==len(sequence)):
        return None
    if(myseqno==-1):
        return False
    if(myseqno!=-1):
        for i in sequence:
            if (i["seqno"] == myseqno+1):
                return i


print findNext(recveddemo,myprogram)
