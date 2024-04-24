import time
import flet as ft
from colorama import Fore

def main(page: ft.Page):
    #Con esto le cambias el fondo a la pagina
    #page.bgcolor = "white"

    #Lo hace centrar vertical
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(ft.Text("Dale Click"))

    def aumento(e):
        text.value = int(text.value) + 1
        #Importando y usando time puede hacer que tarde
        time.sleep(1)
        page.update()

    def disminuir(e):
        text.value = int(text.value) - 1
        page.update()       
        
    #color es el color de la fuente
    #bg color es el color del fondo, y usa hexagesimal
        
    text = ft.TextField("0",color="black",bgcolor="#DDED57")

    page.add(ft.Row(controls=[
        ft.ElevatedButton("+",on_click=aumento),
        text,
        ft.ElevatedButton("-",on_click=disminuir)
        #Con el aligment puede centrar todo
        ], alignment=ft.MainAxisAlignment.CENTER))
    


ft.app(target=main)