import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 350
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_center()

    page.theme_mode = ft.ThemeMode.LIGHT

    def cambio(e):
        if(e.control.value == True):
            page.theme_mode = ft.ThemeMode.DARK
            e.control.label = 'Light Mode'
            page.update()

        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            e.control.label = 'Dark Mode'
            page.update() 

    page.add(ft.Row([
        ft.Switch('Dark Mode',on_change=cambio)
    ],alignment=ft.MainAxisAlignment.CENTER))
    
ft.app(target=main)