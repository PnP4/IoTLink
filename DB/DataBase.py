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
            pass

    def getCon(self):
        self.dbconnection = sqlite3.connect('globalpnp.db')

    def CreateTable(self):
        cursor = self.dbconnection.cursor()
        cursor.execute('''CREATE TABLE metmetadata(name text,ip text, port int,type text)''')
        self.dbconnection.commit()
        self.dbconnection.close()

    def insertInitData(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("Insert INTO metmetadata(name) values('inp')")
        cursor.execute("Insert INTO metmetadata(name) values('out')")
        cursor.execute("Insert INTO metmetadata(name) values('cont')")
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

    

q=SQLDB()
print q.getInputDaemonPort()
print q.getOutputDaemonPort()
print q.getOutputDaemonIP()
