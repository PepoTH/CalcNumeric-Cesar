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
    ,padding=20,margin=-15)

    #256 128 64 32 16 8 4 2 0
    #

    lista = ft.ListView(padding=20,spacing=10,height=250)

    def agregar(e):
        inicio.visible = False
        page.update()
        
        name = ft.TextField(label='Nombre')
        
        def ready(e):
            if(name.value != ""):
                inicio.visible = True
                def detalles(e):
                    print('Detalles')
                    #Continuar con los detalles

                lista.controls.append(ft.OutlinedButton(name.value,on_click=detalles))
                data.visible = False
                page.update()
                
        
        data = ft.Container(ft.Column([
            ft.Text('Ingrese nombre para la factura'),name
            ,ft.FilledButton('Listo',on_click=ready)
        ]))
        
        page.add(data)

        page.update()

    filaADD = ft.Row([
        ft.FilledButton('+',width=300,on_click=agregar)
    ],alignment=ft.MainAxisAlignment.CENTER)


    inicio = ft.Container(ft.Column([
        titulo,lista,filaADD
    ]))

    page.add(inicio)
    
    
ft.app(target=main)
