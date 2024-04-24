import flet as ft

def main(page: ft.Page):

    #Titulo de la ventana
    page.title = "TextField"

    #Agregar un textfield
    #El hint text es un placeholder
    page.add(ft.TextField(bgcolor="WHITE24",hint_text="Clickealo",width=300))

    #Creacion de eventp
    def alclick(e):
        page.add(ft.Text("Clickeado"))

    #Asignandole el evento
    page.add(ft.ElevatedButton(text="Say my name!",on_click=alclick))


ft.app(target=main)