import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 400
    page.window_height = 800
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window_center()

    container = ft.Container(ft.Column([
        ft.Text("Prueba")
    ]))

    page.add(container)
    
ft.app(target=main)
