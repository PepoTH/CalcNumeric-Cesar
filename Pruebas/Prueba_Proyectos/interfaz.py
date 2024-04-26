import flet as ft

def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 600
    page.window_height = 300
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_center()

    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(ft.Row([
        ft.ElevatedButton("Evaluacion 1"),
        ft.ElevatedButton("Evaluacion 2"),
        ft.ElevatedButton("Evaluacion 3")
    ],alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)