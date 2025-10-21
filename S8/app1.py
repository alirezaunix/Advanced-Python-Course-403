import flet as ft


def main(page: ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window.width=300
    page.window.height=200
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    
    def addi(e):
        t1.value=t1.value+1
        page.update()
    
    def removei(e):
        t1.value=t1.value-1
        page.update()

    
    
    t1=ft.TextField(value=0,label="صلوات شمار",cursor_color="#1778D9",cursor_width=5,width=100,text_align=ft.TextAlign.RIGHT)
    b1=ft.IconButton(icon=ft.Icons.ADD,on_click=addi)
    b2=ft.IconButton(icon=ft.Icons.REMOVE,on_click=removei)
    r1=ft.Row(controls=[b2,t1,b1],alignment=ft.MainAxisAlignment.CENTER)
    page.add(r1)
    page.update()



if __name__=="__main__":
    ft.app(main)