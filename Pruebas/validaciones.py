import flet as ft

def main(page: ft.Page):


    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    #tamano de la ventana
    page.window_width = 300
    page.window_height = 300

    #Barra de progreso
    #page.add(ft.ProgressBar(0.5))
    
    #Que no se modifique el tamano
    page.window_resizable = False
    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

ft.app(target=main)