from nicegui import ui

def f1():
    print(in_fname.value)

def f2():
    pass


ui.add_head_html('''
    <style type="text/tailwindcss">
        body{
            background:#00bbff;
        }
    </style>
''')
with ui.row().style("justify-content: center; align-items:center").classes("w-screen"):
    with ui.card().classes("w-1/2"):
        with ui.column().classes("gap-5").classes("w-full"):
            in_fname=ui.input("Firstname").props('clearable').classes("w-full")
            ui.input("Lastname").props('clearable').classes("w-full")
            ui.input("Age").props('clearable').classes("w-full")
            ui.input("Password",password=True,password_toggle_button=True).props('clearable').classes("w-full")
            ui.input("Confirm Password",password=True,password_toggle_button=True).props('clearable').classes("w-full")
            with ui.row().classes("w-full"):
                ui.button(text="OK   ",color="green",on_click=f1).style("flex:2")
                ui.button(text="Clear",color="red",on_click=f2).style("flex:2")


ui.run()