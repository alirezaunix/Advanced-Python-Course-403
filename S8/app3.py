import flet as ft


def main(page: ft.Page):
    page.title = "AppBar Example"


    def changeTheme(e):
        if page.theme_mode==ft.ThemeMode.DARK:
            page.theme_mode=ft.ThemeMode.LIGHT
        else: 
            page.theme_mode=ft.ThemeMode.DARK
        page.update()
        
    
    def newMethod(e):
        t.value=""
        page.open(ft.SnackBar(ft.Text(f"New File ")))
        page.update()
    
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
        
    def saveMethod(e):
        pass
    
    def saveAsMethod(e):
        pass
    
    def openMethod(e):
        pass
    
    def closeMethod(e):
        pass

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.EDIT),
        leading_width=40,
        title=ft.Text("Editor"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED,on_click=changeTheme),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="New",on_click=newMethod),
                    ft.PopupMenuItem(text="Open",on_click=openMethod),
                    ft.PopupMenuItem(text="Save as ..",on_click=saveAsMethod),
                    ft.PopupMenuItem(text="Save",on_click=saveMethod),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Exit",on_click=closeMethod),

                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    t = ft.TextField(multiline=True,max_lines=20,border=ft.InputBorder.NONE,)
    c1=ft.Column(controls=[t],alignment=ft.MainAxisAlignment.CENTER)
    page.add(c1)


ft.app(target=main)