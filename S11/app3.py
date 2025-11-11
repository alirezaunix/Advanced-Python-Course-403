import sqlite3

conn=sqlite3.connect("/Users/alireza/Desktop/Advanced Python Course 403/S11/db.sqlite")
cu=conn.cursor()
cu.execute("DROP TABLE IF EXISTS employees")
cu.execute('CREATE TABLE employees1(id INTEGER PRIMARY KEY,name TEXT,department TEXT)' )
conn.commit()
conn.close()