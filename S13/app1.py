import sqlite3

conn=sqlite3.connect("/Users/alireza/Desktop/Advanced Python Course 403/S13/db2.sqlite")
cu=conn.cursor()
cu.execute("SELECT * FROM student WHERE lname='uu'")
data=cu.fetchall()
print(data)