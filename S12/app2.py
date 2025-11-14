import sqlite3
conn=sqlite3.connect("/Users/alireza/Desktop/Advanced Python Course 403/S12/db.sqlite")
cu=conn.cursor()


fullname=input("Please Enter Your Fullname: ")
dep=input("Please Enter Department: ")

data=[fullname,dep]
cu.execute('INSERT INTO employees1(name,department) VALUES(?,?)' , data)
conn.commit()
conn.close()