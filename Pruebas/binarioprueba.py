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

    def accion(e):
        for i in range(0,len(txt.value) - 1):
            #Algoritmo de respuesta aqui 
            print("hola")

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