import flet as ft

def main(page: ft.Page):

    page.window_resizable = False

    txt = ft.Text('Hi')

    #Solo se pueden controlar valores de coordenadas con stack y poniendole top y left siendo
    #x e y, top el espacio hacia arriba del componente y left el espacio hacia la izquierda

    stack = ft.Stack([
        ft.Row([
            txt,ft.TextField()
        ],top=60,left=300),
        ft.Row([
            ft.Text('Mundo'),ft.TextField()
        ],top=60,left=30),
    ])
    
    page.add(stack)
    
ft.app(target=main)