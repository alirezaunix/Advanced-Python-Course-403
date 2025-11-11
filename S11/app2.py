from nicegui import ui

@ui.page('/other_page')
def other_page():
    ui.label('Welcome to the other side')

@ui.page('/dark_page', dark=True)
def dark_page():
    ui.label('Welcome to the dark side')

@ui.page('/')
def page():
    ui.link('Visit other page', other_page)
    ui.link('Visit dark page', dark_page)

ui.run()