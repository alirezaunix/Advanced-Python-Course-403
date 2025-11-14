import sqlite3
conn=sqlite3.connect("/Users/alireza/Desktop/Advanced Python Course 403/S12/db.sqlite")
cu=conn.cursor()




data=(1,'alireza','it')
cu.execute('INSERT INTO employees1(id,name,department) VALUES(?,?,?)' , data)
conn.commit()
conn.close()