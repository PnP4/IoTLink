import json
import os

import sys
from termcolor import colored, cprint
path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(path)

import netifaces

from DB.DataBase import SQLDB
from ControlDeamonListen.ControlMessageHandler import MessageHandle

class RecoverDaemon:
    def __init__(self):
        try:
            self.myips = self.getAllInterfaceAddresses()  # This will be keep all his ips.
            self.db=SQLDB()
            path = os.getenv("HOME") + "/MetaPnpGlobal"
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = path + "/config.json"
            jsfile = open(filepath, "r")
            self.myreqjson =json.load(jsfile)
            path = os.getenv("HOME") + "/MetaPnpGlobal"
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = path + "/configseq.json"
            jsfile = open(filepath, "r")
            self.myseqjson = json.load(jsfile)

            self.myid=self.myreqjson["you"]
            #return  True
        except Exception as e:
            print e
            self.myreqjson=None
            self.myseqjson=None

    def getNextScans(self):
        if(self.myreqjson is None or self.myseqjson is None):
            return False
        else:
            reply = {}
            name=self.db.getMyName()
            ###REPLICATE FROM DEAMONLISTENR
            handle=MessageHandle()
            nextList = handle.getNextNodes(self.myreqjson)
            if (nextList != None):  # This is not an end node
                cprint('Not Last', 'green')
                self.myreqjson["you"] = handle.findNext(self.myreqjson, self.myreqjson["you"])[
                    "name"]  # change the next node's you tag.
                for node in nextList:  # check all nodes sequentially for the availability
                    cprint('an node ' + node.getip(), 'green')
                    if (not self.filetrOutSelfIps(node)):
                        # print "Done"
                        cprint('not loop', 'green')

                        msg = self.conectToNextNode(node, self.myreqjson)  # This means the node is available
                        if (msg):
                            cprint('msg up', 'green')
                            # print msg
                            print "======================"
                            if (not ("Fail" in json.loads(msg)["msg"])):
                                cprint('Fail not in', 'green')
                                tempjm = json.loads(msg)
                                tempjm["ip"] = node.getip()
                                reply["next"] = tempjm
                                # print "------ ",msg
                                break
                            else:
                                cprint('Fail in', 'green')
                        else:
                            cprint('msg is False', 'green')
                            pass
                    else:
                        cprint('loop broo', 'green')
                        print "Loop detected"
            else:  # ToDo NEED TO GET THE PROGRAM NAME FROM THE MESSAGE
                cprint('Last', 'green')
                # print "HEY AM I THE LAST ONE?"
                pass

            repmsg = json.dumps(reply)
            print repmsg

            ##########END REPLICATE DEAMON LISTNER

    def getAllInterfaceAddresses(self):  # get the idea of the network address of the node has.
        iplist = []
        interface_list = netifaces.interfaces()
        for iname in interface_list:
            if (("eth" in iname) or ("wlan" in iname)):  # get only eth and wlan (ethernet and wifi addresses)
                try:
                    internetIps = netifaces.ifaddresses(iname)[netifaces.AF_INET]  # fetch only IPv4 address only
                    iplist.append(internetIps[0]["addr"])
                except:
                    pass
        return iplist

    def filetrOutSelfIps(self, node):

        if (node.getip() in self.myips):
            return True
        if ("127.0." in node.getip()):
            return True
        return False

    def conectToNextNode(self, NextNode, msg):
        try:
            return NextNode.checkStatus(msg)

        except:
            return False


p=RecoverDaemon()
p.getNextScans()



