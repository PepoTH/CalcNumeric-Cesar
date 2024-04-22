import flet as ft

def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 300
    page.window_height = 300

    #Poner todo centrado
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Con este metodo pones la ventana al medio
    page.window_center()

    def login(e):
        page._dispose()

    page.add(ft.Container(ft.Column([
        ft.ElevatedButton("Iniciar Sesion",width=150,on_click=login),
        ft.ElevatedButton("Registrar",width=150)
    ])))

    
ft.app(target=main)