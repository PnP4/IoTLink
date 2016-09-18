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
        except:
            pass

    def getCon(self):
        self.dbconnection = sqlite3.connect('globalpnp.db')

    def CreateTable(self):
        cursor = self.dbconnection.cursor()
        cursor.execute('''CREATE TABLE netmetadata(name text,ip text, port int,type text)''')
        self.dbconnection.commit()
        self.dbconnection.close()

    def insertInitData(self):
        self.getCon()
        cursor = self.dbconnection.cursor()
        cursor.execute("Insert INTO netmetadata(name) values('inp')")
        cursor.execute("Insert INTO netmetadata(name) values('out')")
        cursor.execute("Insert INTO netmetadata(name) values('cont')")
        self.dbconnection.commit()
        self.dbconnection.close()





