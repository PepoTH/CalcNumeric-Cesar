import flet as ft

def main(page: ft.Page):

    #Creacion de Ventana
    page.window_resizable = False
    page.padding = 30

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #Evento que agregue el texto del txtField
    def agregar(e):
        if(txt.value == ""):
            txt.error_text = "Ingrese una Tarea"
        else:
            l.controls.append(ft.Checkbox(label=txt.value))
            txt.value = ""

        page.update()

    def eliminar(e):
        print("Eliminar")

    #Creacion de Elementos
    txt = ft.TextField(label="Tarea",width=400)
    l = ft.ListView(expand=1,padding=30)
    add = ft.ElevatedButton("Add",on_click=agregar)
    delete = ft.ElevatedButton("Delete",on_click=eliminar)

    #Agregando los elementos
    page.add(ft.Row(controls=[
        txt,add,delete
    ],alignment=ft.MainAxisAlignment.CENTER),ft.RadioGroup(content=l))


    
ft.app(target=main)