import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 400
    page.window_height = 500
    page.padding = 30
    
    page.theme_mode = ft.ThemeMode.LIGHT

    txt = ft.TextField(label='Buscar')

    titulo = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text("Facturacion")
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                txt
            ],alignment=ft.MainAxisAlignment.CENTER)
        ])
    ,padding=20,margin=-10)

    #256 128 64 32 16 8 4 2 0
    #

    lista = ft.ListView(padding=20,spacing=10,height=250)

    filaADD = ft.Row([
        ft.FilledButton('+',width=300)
    ],alignment=ft.MainAxisAlignment.CENTER)

    page.add(titulo,lista,filaADD)

    for i in range(0,20):
        lista.controls.append(ft.OutlinedButton('Hola'))
        lista.update()

    
    
ft.app(target=main)
