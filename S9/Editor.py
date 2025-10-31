import flet as ft

def main(page: ft.Page):
    page.title = "AppBar Example"
    filename=""
    # ✅ variable to store full path of file chosen in SaveAs
    saveas_full_path = {"value": None}

    selected_files = ft.Text()

    def pick_files_result(e: ft.FilePickerResultEvent):
        # ✅ If save-as was done, this contains full path (e.path)
        if e.path:
            saveas_full_path["value"] = e.path
            print("SAVE AS FULL PATH =", saveas_full_path["value"])
            filename=saveas_full_path["value"]

        # ✅ This part still updates selected_files for open()
        selected_files.value = (
            ", ".join(f.name for f in e.files) if e.files else "Cancelled!"
        )
        selected_files.update()

    file_picker = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(file_picker)

    def changeTheme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    def newMethod(e):
        t.value = ""
        page.open(ft.SnackBar(ft.Text("New File")))
        page.update()

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def saveMethod(e):
        # ✅ later you can use saveas_full_path["value"] here
        #print("SAVE TO:", saveas_full_path["value"])
        #str1=t.value
        #f1=open(saveas_full_path["value"],"ta")
        #f1.write(str1)
        #f1.close()
        print(saveas_full_path["value"])
        
        
    def saveAsMethod(e):
        #str1=t.value
        #f1=open(saveas_full_path["value"],"tw")
        #f1.write(str1)
        #f1.close()
        file_picker.save_file()
        print(filename)

        
    def openMethod(e):
        file_picker.pick_files()
        # Note: print inside pick_files_result will show the selection
        # this print just prints "None" because pick_files() returns nothing
        print(file_picker.pick_files())

    def closeMethod(e):
        page.window_close()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.EDIT),
        leading_width=40,
        title=ft.Text("Editor"),
        center_title=False,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED,on_click=changeTheme),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="New",on_click=newMethod),
                    ft.PopupMenuItem(text="Open",on_click=openMethod),
                    ft.PopupMenuItem(text="Save as ..",on_click=saveAsMethod),
                    ft.PopupMenuItem(text="Save",on_click=saveMethod),
                ]
            ),
        ],
    )

    t = ft.TextField(multiline=True,max_lines=20,border=ft.InputBorder.NONE)
    page.add(t, selected_files)

ft.app(target=main)
