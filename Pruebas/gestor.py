import flet as ft

def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 300
    page.window_height = 400
    page.title = "Gestor de Archivos"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.LIGHT

    picker = ft.FilePicker()
    btn = ft.ElevatedButton("Escoger",on_click=picker.pick_files)
    
    page.add(ft.Row([btn,picker],alignment=ft.MainAxisAlignment.CENTER))
    
ft.app(target=main)