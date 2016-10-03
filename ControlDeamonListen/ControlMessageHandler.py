

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

