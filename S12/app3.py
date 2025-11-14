import sqlite3

conn=sqlite3.connect("/Users/alireza/Desktop/Advanced Python Course 403/S12/db2.sqlite")
cu=conn.cursor()

fname=input("pleas enter your first name: ")
lname=input("pleas enter last name: ")
yearofbirth=input("plear enter your birth date: ")
nationalcode=input("pleas enter your national code: ")


cu.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT,lname TEXT,yearofbirth INTEGER ,nationalcode TEXT )")
cu.execute(f"INSERT INTO student(fname,lname,yearofbirth,nationalcode) VALUES(?,?,?,?)",[fname,lname,yearofbirth,nationalcode])
conn.commit()
conn.close()

