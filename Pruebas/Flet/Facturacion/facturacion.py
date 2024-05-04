import flet as ft
import factura

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 400
    page.window_height = 500
    page.padding = 30
    
    page.theme_mode = ft.ThemeMode.LIGHT

    def buscador(e):
        if(len(lista.controls) != 0):
            if(txt.value != ""):
                for i in range(0,len(lista.controls)):
                    if(txt.value in lista.controls[i].text):
                        print(lista.controls[i].text)
                        lista.controls[i].focus()
                
                   
        
                    

                    

    txt = ft.TextField(label='Buscar',on_change=buscador)

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

    lista = ft.ListView(padding=20,spacing=10,height=250)

    def agregar(e):
        inicio.visible = False
        page.update()
        
        name = ft.TextField(label='Nombre')
        
        def ready(e):
            if(name.value != ""):
                inicio.visible = True
                def detalles(e):
                    alerta = ft.BottomSheet(
                        ft.Container(
                            ft.Column([
                                ft.Text(e.control.text)
                            ]),width=300,height=200,padding=30
                        )
                        ,open=True
                    )
                    page.overlay.append(alerta)
                    page.update()
                    #Continuar con los detalles

                fact = factura.factura(name.value)

                lista.controls.append(ft.OutlinedButton(fact.getName(),on_click=detalles))
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
