import flet as ft

def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 300
    page.window_height = 400
    page.title = "Gestor de Archivos"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(ft.FilePicker())
    
ft.app(target=main)