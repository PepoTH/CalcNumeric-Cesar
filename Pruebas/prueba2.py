import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 300
    page.padding = 30
    
    
    page.window_center()

    txt = ft.TextField()

    page.add(txt,ft.top)
    
ft.app(target=main)