import time
import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 450
    page.window_height = 400
    page.padding = 30
    
    page.theme_mode = ft.ThemeMode.LIGHT

    def gauss(e):
        _main_.visible = False
        gauss.visible = True
        page.update()

    def conv(e):
        _main_.visible = False
        page.add(conversiones)
        conversiones.visible = True
        page.update()

    gaussiana = ft.Container()

    conversiones = ft.Container(
        ft.Row([
            ft.Text('Sistemas Numericos',weight=ft.FontWeight.W_500,
                    font_family='Poppins',size=15)
        ],alignment=ft.MainAxisAlignment.CENTER)
    )

    conversiones.visible = False
    gaussiana.visible = False

    btns = ft.Row([
            ft.FilledButton('Gaussiana',on_click=gauss),
            ft.FilledButton('Convertir',on_click=conv)
    ],alignment=ft.MainAxisAlignment.CENTER)

    _main_ = ft.Container(
        content=ft.Column([
            ft.Text('Evaluaciones',font_family='Poppins',size=20)
            ,btns
        ],alignment=ft.MainAxisAlignment.CENTER
        ,horizontal_alignment=ft.CrossAxisAlignment.CENTER,height=page.height/2)
    )
    page.add(_main_)
     
ft.app(target=main)