import sqlite3

conn = sqlite3.connect('globalpnp.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE netmetadata(name text,ip text, port int,type text)''')

cursor.execute("Insert INTO netmetadata(name) values('inp')")
cursor.execute("Insert INTO netmetadata(name) values('out')")
cursor.execute("Insert INTO netmetadata(name) values('cont')")

conn.commit()
conn.close()