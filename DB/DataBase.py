import sqlite3

conn = sqlite3.connect('globalpnp.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE netmetadata(ip text, port int,type text)''')


conn.commit()
conn.close()