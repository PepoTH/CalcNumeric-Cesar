import math
import flet as ft


def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 300
    page.window_height = 300
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_center()

    page.theme_mode = ft.ThemeMode.LIGHT

    def binario(n):
        dec = 0
        if("." in str(n)):
            dec = round((n - int(n)),4)
            n = math.trunc(n)
            
        num = ""
        while(n > 0):
            num = str(n % 2) + num
            n = n // 2

        if(n == 0) :
            num = str(0) + num
        num = num + "."

        cont = 0
        while(cont < 4):
            num = num + str(math.trunc(dec * 2))
            dec = round(((dec * 2) - int(dec * 2)),4)
            cont += 1

        #Falta simplificar en caso que solo sea entero

        return num
    
    def decimal(n):
        #Agregar binario a decimal
        pass

    def accion(e):
        print(binario(float(txt.value)))
        txt.update()

    def cambio(e):
        #Algoritmo que elimina todo excepto numeros y un solo punto
        if(txt.value != ""):
            #Para solo dejar entrar teclas que no son numeros
            if not(txt.value[len(txt.value ) - 1].isdecimal()):
                #Eliminacion del punto
                if(txt.value[len(txt.value ) - 1] == "."):
                    cont = 0
                    #Ciclo buscador de varios puntos
                    for i in range(0,len(txt.value) - 1):
                        if(txt.value[i] == "."):
                            cont += 1

                    if(cont == 1):
                        txt.value = txt.value[0:len(txt.value) - 1]

                else:
                    #Eliminacion de la letra o todo lo demas
                    txt.value = txt.value.replace(txt.value[-1],"")
                
            txt.update()

    txt = ft.TextField(text_align="left",on_change=cambio,hint_text="Ingrese un numero")

    page.add(txt,ft.ElevatedButton("Convertir",on_click=accion))
    
ft.app(target=main)