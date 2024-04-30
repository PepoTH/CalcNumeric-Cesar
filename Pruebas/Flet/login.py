import flet as ft
import time

def main(page: ft.Page):
    page.title = "Login"
    page.window_resizable = False
    page.padding = 50
    

    page.window_width = 300
    page.window_height = 300

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt = ft.TextField(hint_text="Ingrese su correo",
                       label="Correo"
                       )

    def log(e):
        page.clean()
        pb = ft.ProgressBar(0)
        page.add(pb)
        for i in range(10,101):
            time.sleep(0.1)
            pb.value= i/100
            
            page.update()

        if(pb.value == 1):
            page.add(ft.Text("Completado!"))
        

    row = ft.Row(controls=[
        ft.ElevatedButton("Login",on_click=log),
        ft.ElevatedButton("Register")
    ],alignment=ft.MainAxisAlignment.CENTER)

    page.add(txt,row)

ft.app(target=main)