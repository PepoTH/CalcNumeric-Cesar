import flet as ft
import factura

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 400
    page.window_height = 500
    page.padding = 30
    
    page.theme_mode = ft.ThemeMode.LIGHT

    def listo(e):
        if(txtDelete.value != ''):
            lista.controls.remove(ft.OutlinedBorder(text=txtDelete.value))
            page.update()
        pass

    def delete(e):
        fil.visible = True
        lista.height = 200
        page.update()
        pass

    def buscador(e):
        if(len(lista.controls) != 0):
            if(txt.value != ""):
                for i in range(0,len(lista.controls)):
                    if(txt.value in lista.controls[i].text):
                        lista.controls[i].focus()               

    txt = ft.TextField(label='Buscar',on_change=buscador)

    titulo = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text("Citas")
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
        entrega = ft.TextField(label='Apellido')
        destinatario = ft.TextField(label='Numero')
        encargado = ft.TextField(label='Fecha')
        cantidad = ft.TextField(label='Hora')
    
        def ready(e):
            if name.value!= "":
                inicio.visible = True
                fact = factura.factura(**{
                    'name': name.value,
                    'entrega': entrega.value,
                    'destinatario': destinatario.value,
                    'encargado': encargado.value,
                    'cantidad': cantidad.value
                })
            
                def detalles(e):
                    print(e.control)
                    alerta = ft.BottomSheet(
                        ft.Container(
                            ft.Column([
                                ft.Text(f"Nombre: {fact.getName()}"),
                                ft.Text(f"Apellido: {fact.getFechaEntrega()}"),
                                ft.Text(f"Numero: {fact.getDestinatario()}"),
                                ft.Text(f"Fecha: {fact.getEncargado()}"),
                                ft.Text(f"Hora: {fact.getCantidad()}")
                            ]), width=300, height=200, padding=30
                        ),
                        open=True
                    )
                    page.overlay.append(alerta)
                    page.update()


                lista.controls.append(
                        ft.OutlinedButton(fact.getName()
                                    , on_click=detalles,width=250))
                                    
                data.visible = False
                page.update()
    
        data = ft.Container(ft.Column([
            ft.Text('Ingrese datos para la factura'), name,
            entrega, destinatario, encargado, cantidad,
            ft.FilledButton('Listo', on_click=ready)
        ]))
    
        page.add(data)
    
        page.update()

    filaADD = ft.Row([
        ft.FilledButton('+',width=250,on_click=agregar),
        ft.IconButton(ft.icons.DELETE,on_click=delete)
    ],alignment=ft.MainAxisAlignment.CENTER)


    inicio = ft.Container(ft.Column([
        titulo,lista,filaADD
    ]))
    txtDelete = ft.TextField(width=250)
    fil = ft.Row([
            txtDelete,
            ft.IconButton(ft.icons.CHECK,listo)
        ],alignment='center')
    
    fil.visible = False

    page.add(inicio,fil)
    
    
ft.app(target=main)
