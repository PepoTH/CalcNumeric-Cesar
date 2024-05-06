
import time
import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 350
    page.window_height = 700
    page.padding = 30
    
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window_center()

    #Algoritmo de Validacion de los Textfield
    def valid(e):
        if(len(e.control.value) > 1):
            e.control.value = e.control.value[0]
            e.control.update()

        if(e.control == txt1): txt2.focus()
        if(e.control == txt2): txt3.focus()
        if(e.control == txt3): txt4.focus()

        #Validar el Codigo real
        if("".join([txt1.value,txt2.value,txt3.value,txt4.value]) == "2004"):
            txt1.disabled = True
            txt2.disabled = True
            txt3.disabled = True
            txt4.disabled = True
            pb = ft.ProgressBar(0,border_radius=20)
            page.add(pb)

            #Aumentando barra de progreso
            for i in range(0,101):
                pb.value = i / 100
                time.sleep(0.01)
                pb.update()

            #Continuar desde aqui con la siguiente seccion
            
            print("Inicializando")
            

    #Agregando Texfields
    txt1 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    txt2 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    txt3 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    txt4 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    
    row = ft.Row([
        txt1,
        txt2,txt3,txt4
    ],alignment=ft.MainAxisAlignment.CENTER)

    page.add(ft.Container(ft.Column(
        [
            ft.Text("Login",size=30,font_family="Poppins"),
            ft.Text("Ingrese el codigo"),
            row
        ],alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )))


ft.app(target=main)