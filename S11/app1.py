from nicegui import ui
import sqlite3


@ui.page('/other_page')
def other_page():
    data=[]
    for line in open("/Users/alireza/Desktop/Advanced Python Course 403/S11/data.csv"):
        data.append(dict(zip(["Firstname","Lastname","Age"],line.split(","))))
    
    
    
    with ui.row().style("justify-content: center; align-items:center").classes("w-screen"):
        with ui.card().classes("w-1/2"):
            ui.table(rows=data).classes("w-full")

            with ui.column().classes("gap-5").classes("w-full"):
                with ui.row().classes("w-full"):
                    ui.button(text="Back",color='blue',on_click=lambda: ui.navigate.to("/")).style("flex:1")


@ui.page('/')
def main():

    ui.add_head_html('''
        <style type="text/tailwindcss">
            body{
                background:#00bbff;
            }
        </style>
    ''')
        
    def f1():
        fname=in_fname.value
        lname=in_lname.value
        age=in_age.value
        pass1=in_pass.value
        pass2=in_pass_2.value
        if pass1!=pass2:
            ui.notify("Password in Not Match")
        elif len(pass1)<8:
            ui.notify("Password Length must be over 8")
        #with open("/Users/alireza/Desktop/Advanced Python Course 403/S11/data.csv","ta") as f1:
        #    f1.write(f"{fname},{lname},{age},{pass1}\n")
        conn=sqlite3.connect("/Users/alireza/Desktop/Advanced Python Course 403/S11/db.sqlite")
        cu=conn.cursor()
        cu.execute("CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,age INTEGER,pass TEXT)")
        cu.execute('INSERT INTO person(fname,lname,age,pass) VALUES(?,?,?,?)',[fname,lname,age,pass1])
        conn.commit()
        conn.close()
        f2()
    
    def f2():
        in_fname.value=""
        in_lname.value=""
        in_age.value=""
        in_pass.value=""
        in_pass_2.value=""

    with ui.row().style("justify-content: center; align-items:center").classes("w-screen"):
        with ui.card().classes("w-1/2"):
            with ui.column().classes("gap-5").classes("w-full"):
                in_fname=ui.input("Firstname").props('clearable').classes("w-full")
                in_lname=ui.input("Lastname").props('clearable').classes("w-full")
                in_age=ui.input("Age").props('clearable').classes("w-full")
                in_pass=ui.input("Password",password=True,password_toggle_button=True).props('clearable').classes("w-full")
                in_pass_2=ui.input("Confirm Password",password=True,password_toggle_button=True).props('clearable').classes("w-full")
                with ui.row().classes("w-full"):
                    ui.button(text="OK   ",color="green",on_click=f1).style("flex:2")
                    ui.button(text="Clear",color="red",on_click=f2).style("flex:2")
                with ui.row().classes("w-full"):
                    ui.button(text="Show Data",color="blue",on_click=lambda: ui.navigate.to("/other_page")).style("flex:1")
                    
ui.run()