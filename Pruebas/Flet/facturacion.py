import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 400
    page.window_height = 500
    page.padding = 30
    
    page.theme_mode = ft.ThemeMode.LIGHT

    txt = ft.TextField()

    contenedor = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text("Facturacion")
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                txt
            ],alignment=ft.MainAxisAlignment.CENTER)
        ])
    ,bgcolor='red',height=page.window_height*0.8,padding=20)

    page.add(contenedor)
    
ft.app(target=main)
