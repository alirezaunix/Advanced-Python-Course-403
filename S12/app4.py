import sqlite3

conn=sqlite3.connect("/Users/alireza/Desktop/Advanced Python Course 403/S12/db2.sqlite")
cu=conn.cursor()
cu.execute("SELECT * FROM student ORDER BY fname")
data=cu.fetchall()
print(data)