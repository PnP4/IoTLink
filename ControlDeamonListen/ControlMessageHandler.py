import json


class MessageHandle:


    def findNext(self,fulljson, myprogram):
        sequence = fulljson["seq"]
        myseqno = -1
        for i in sequence:
            if (i["name"] == myprogram):
                myseqno = i["seqno"]
                break
        if (myseqno == len(sequence)):
            return None
        if (myseqno == -1):
            return False
        if (myseqno != -1):
            for i in sequence:
                if (i["seqno"] == myseqno + 1):
                    return i

    def getNextNodes(self,fulljson):
        myprg=fulljson["you"]
        nextmeta=self.findNext(fulljson,myprg)
        if(nextmeta!=None):
            return fulljson[nextmeta["name"]]
        else:
            return None




data={}
data["seq"]=[{"seqno":1,"name":"a"},{"seqno":2,"name":"b"},{"seqno":3,"name":"c"},{"seqno":4,"name":"d"}]
data["you"]="b"
data["a"]=[{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090}]
data["b"]=[{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090}]
data["c"]=[{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090}]
data["d"]=[{"ip":"127.0.0.1","conport":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090},{"ip":"127.0.0.1","port":8080,"avialable":0,"inport":8090}]

print json.dumps(data)

msg=json.dumps(data)


recveddemo=json.loads(msg)

a=MessageHandle()
print a.getNextNodes(recveddemo)



