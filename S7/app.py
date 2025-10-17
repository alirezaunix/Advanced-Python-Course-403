import flet as ft

def main(page: ft.Page):
    page.title = "My App"
    page.bgcolor="#0C88F4"
    page.window.width=400
    page.window.height=300
    page.window.minimizable=False
    page.window.maximizable=False
    page.theme_mode=ft.ThemeMode.LIGHT
    
    t1 = ft.Text(value="Hello, world!", color="#042644",size=30,bgcolor="#86B8E3")
    t2=ft.Text(value="Silly Girls!!",color="#7339E0",weight=ft.FontWeight.BOLD)
    
    cont1=ft.Container(content=t1,
                    margin=10,
                    padding=20,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
)
    
    cont2=ft.Container(content=t2,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    )
    
    
    r1=ft.Row(controls=[cont1,cont2])
    
    t3=ft.FilledTonalButton(text="Filled tonal button")

    r2=ft.Row(controls=[t3])
    
    c1=ft.Column(controls=[r1,r2])
    
    page.add(c1)
    page.update()

if __name__=="__main__":
    ft.app(main)