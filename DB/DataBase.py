import sqlite3



class SQLDB:
    def __init__(self):
        try:
            self.getCon()
        except:
            pass

        try:
            self.CreateTable()
        except:
            pass

        try:
            self.insertInitData()
        except Exception as e:
            print e
            pass

    def getCon(self):
        self.dbconnection = sqlite3.connect('globalpnp.db')

    def CreateTable(self):
        cursor = self.dbconnection.cursor()
        cursor.execute('''CREATE TABLE metmetadata(name text primary key,ip text, port int,type text)''')
        cursor.execute('''CREATE TABLE snapdata(keyname text primary key,data text)''')
        self.dbconnection.commit()
        self.dbconnection.close()

    def insertInitData(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("Insert INTO metmetadata(name,port) values('inp',8200)")
        cursor.execute("Insert INTO metmetadata(name,port) values('out',8500)")
        cursor.execute("Insert INTO metmetadata(name,port) values('cont',8100)")
        cursor.execute("Insert INTO snapdata(keyname,data) values('status','avialable')")
        cursor.execute("Insert INTO snapdata(keyname) values('prgid')")
        cursor.execute("Insert INTO snapdata(keyname,data) values('programs','a|b|c|d')")
        self.dbconnection.commit()
        self.dbconnection.close()

    def getInputDaemonPort(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("SELECT port FROM metmetadata WHERE name = 'inp'")
        return cursor.fetchone()[0]

    def getOutputDaemonPort(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("SELECT port FROM metmetadata WHERE name = 'out'")
        return cursor.fetchone()[0]

    def getOutputDaemonIP(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("SELECT ip FROM metmetadata WHERE name = 'out'")
        return cursor.fetchone()[0]

    def getControlDaemonPort(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("SELECT port FROM metmetadata WHERE name = 'cont'")
        return cursor.fetchone()[0]

    def getStatus(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("SELECT data FROM snapdata WHERE keyname = 'status'")
        return cursor.fetchone()[0]

    def getprgid(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("SELECT data FROM snapdata WHERE keyname = 'prgid'")
        return cursor.fetchone()[0]

    def getprograms(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("SELECT data FROM snapdata WHERE keyname = 'programs'")
        return cursor.fetchone()[0]

    def isPrgInMe(self,prg):
        prs=self.getprograms()
        prs=prs.split("|")
        if (prg in prs):
            return True
        return False


a=SQLDB()
print a.getOutputDaemonPort()
print a.getInputDaemonPort()
print a.getprograms()
print a.getControlDaemonPort()
print a.getOutputDaemonIP()
print a.isPrgInMe("a")
print a.isPrgInMe("z")
print a.getprgid()
