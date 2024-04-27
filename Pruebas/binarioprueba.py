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
        if(txt.value != ""):
            texto = ["Hola"]
            texto.remove("Hola")
            
            print(texto)

    def cambio(e):
        if(txt.value != ""):
            if not(txt.value[len(txt.value) - 1].isdecimal()):
                txt.value = txt.value.replace(txt.value[-1],"")
                txt.update()
            
            

    txt = ft.TextField(text_align="right",on_change=cambio)

    page.add(txt,ft.ElevatedButton("Convertir",on_click=accion))
    
ft.app(target=main)