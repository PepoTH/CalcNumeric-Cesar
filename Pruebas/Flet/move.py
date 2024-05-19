import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 300
    
    page.window_center()
    
ft.app(target=main)