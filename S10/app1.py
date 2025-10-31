from nicegui import ui

with ui.column().classes("gap-3; w-full"):
    ui.button(text="OK",color="red").classes("w-full")
    ui.button(text="OK",color="yellow").classes("w-1/2")
    ui.button(text="OK",color="blue").classes("w-1/4")
    ui.button(text="OK",color="green").classes("w-1/8")
ui.separator()
with ui.row().classes("gap-3; w-full"):
    ui.button(text="OK",color="red").classes("w-full")
    ui.button(text="OK",color="yellow").classes("w-1/2")
    ui.button(text="OK",color="blue").classes("w-1/4")
    ui.button(text="OK",color="green").classes("w-1/8")



ui.run()