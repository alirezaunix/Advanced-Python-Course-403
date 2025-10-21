import flet as ft


def main(page: ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.bgcolor="#063768"
    page.window.width=300
    page.window.height=400
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    
    
    def registerMethod(e):
        f1=open("/Users/alireza/Desktop/Advanced Python Course 403/S8/data.csv","ta")
        out=f"{txt_fname.value},{txt_lname.value},{txt_age.value}\n"
        f1.write(out)
        f1.close()
        clearMethod(e)
    
    def clearMethod(e):
        txt_fname.value=""
        txt_lname.value=""
        txt_age.value=""
        page.update()
    
    
    txt_fname=ft.TextField(label="Firstname",cursor_color="#1778D9",cursor_width=5,width=250,color="#EDA20A")
    txt_lname=ft.TextField(label="Lastname",cursor_color="#1778D9",cursor_width=5,width=250,color="#EDA20A")
    txt_age=ft.TextField(label="Age",cursor_color="#1778D9",cursor_width=5,width=250,color="#EDA20A")
    r1=ft.Row(controls=[txt_fname],alignment=ft.MainAxisAlignment.CENTER)
    r2=ft.Row(controls=[txt_lname],alignment=ft.MainAxisAlignment.CENTER)
    r3=ft.Row(controls=[txt_age],alignment=ft.MainAxisAlignment.CENTER)
    
    
    
    b1=ft.FilledButton(text="Register",width=120,bgcolor="#0958A8",on_click=registerMethod)
    b2=ft.FilledButton(text="Clear",width=120,bgcolor="#E82610",on_click=clearMethod)
    r4=ft.Row(controls=[b1,b2],alignment=ft.MainAxisAlignment.CENTER)
    page.add(r1,r2,r3,r4)
    page.update()


if __name__=="__main__":
    ft.app(main)#view=ft.AppView.WEB_BROWSER