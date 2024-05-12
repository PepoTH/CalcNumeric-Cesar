import flet as ft
import time
from funciones import *

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
        conversiones.visible = True
        page.update()

    def back(e):
        _main_.visible = True
        gauss.visible = False
        conversiones.visible = False
        page.update()     

    def convert(e):
        if(txt.value != '' and opciones.value != None):
            print(str(sistemas(txt.value,opciones.value)))

    def clear(e):
        txt.value = ''
        opciones.value = None
        page.update()

    gaussiana = ft.Container()
    txt = ft.TextField(width=page.width*0.3,label='Introduzca un Numero',
                       border_color='#E1E1E1',border_radius=10)
    
    opciones = ft.Dropdown(width=page.width*0.15,border_color='#E1E1E1'
                                ,border_radius=10,hint_text='N/A',options=[
                                    ft.dropdown.Option('Dec'),
                                    ft.dropdown.Option('Bin'),
                                    ft.dropdown.Option('Oct'),
                                    ft.dropdown.Option('Hex')
                                ])
    
    conversiones = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text('Sistemas Numericos',weight=ft.FontWeight.W_500,
                    font_family='Poppins',size=15)
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([
                ft.Row([
                    txt,opciones
                        ],alignment='center'),
                ft.Row([
                    ft.FilledButton('Convertir'
                                ,style=ft.ButtonStyle(bgcolor='#6F86FF'),
                                    width=270,on_click=convert),
                    ft.IconButton(ft.icons.DELETE,icon_color='#6F86FF',on_click=clear),
                    ft.IconButton(ft.icons.LIST,disabled=True,icon_color='#6F86FF')
                        ],alignment='center')
            ],alignment=ft.MainAxisAlignment.CENTER)

            ,ft.Row([
                ft.IconButton(ft.icons.EXIT_TO_APP,on_click=back,icon_color='#6F86FF')
            ],vertical_alignment=ft.MainAxisAlignment.END)
        ],spacing=75,alignment='center')
    )
    gaussiana.visible = False

    btns = ft.Row([
            ft.FilledButton('Gaussiana',style=ft.ButtonStyle(bgcolor='#6F86FF'),on_click=gauss),
            ft.FilledButton('Convertir',style=ft.ButtonStyle(bgcolor='#6F86FF'),on_click=conv)
    ],alignment=ft.MainAxisAlignment.CENTER)

    _main_ = ft.Container(
        content=ft.Column([
            ft.Text('Evaluaciones',font_family='Poppins',size=20)
            ,btns
        ],alignment=ft.MainAxisAlignment.CENTER
        ,horizontal_alignment=ft.CrossAxisAlignment.CENTER,height=page.height/2)
    )

    conversiones.visible = False

    page.add(_main_,conversiones)
    
ft.app(target=main)