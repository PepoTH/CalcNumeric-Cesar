import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 450
    page.padding = 30

    #Cambiando el tema
    page.theme_mode = ft.ThemeMode.DARK

    txt = ft.TextField(
        hint_text="0",text_align="right")
    page.add(txt)

    def click(e):
        txt.value = txt.value + e.control.text
        txt.update()
        
    def operations(e):
        if (txt.value[-1] not in ("+", "-")):
            #Con e.control consigues el boton o el source
            if(e.control == mas):
                txt.value = txt.value + "+"
            elif(e.control == menos):
                txt.value = txt.value + "-"
            elif(e.control == multiply):
                txt.value = txt.value + "*"
            elif(e.control == division):
                txt.value = txt.value + "/"
        txt.update()

    def equals(e):
        txt.value = str(float(eval(txt.value)))
        txt.update()

    def borrar(e):
        txt.value = ""
        txt.update()

    for i in range(1,10,3):
        page.add(ft.Row([
            ft.ElevatedButton(f"{i}",width=65,height=50,on_click=click),
            ft.ElevatedButton(f"{i + 1}",width=65,height=50,on_click=click),
            ft.ElevatedButton(f"{i + 2}",width=65,height=50,on_click=click)
        ],alignment=ft.MainAxisAlignment.CENTER))

    mas = ft.IconButton(ft.icons.ADD,on_click=operations,width=40,height=40)
    menos = ft.IconButton(ft.icons.INDETERMINATE_CHECK_BOX,on_click=operations,width=40,height=40)
    igual = ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,on_click=equals,width=40,height=40)
    borrar = ft.IconButton(ft.icons.DELETE,on_click=borrar,width=40,height=40)
    multiply = ft.IconButton(ft.icons.CLOSE,on_click=operations,width=40,height=40)
    division = ft.IconButton(ft.icons.PERCENT,on_click=operations,width=40,height=40)

    page.add(ft.Row([
        mas,menos,multiply,division
    ],alignment=ft.MainAxisAlignment.CENTER))

    page.add(ft.Row([
        igual,borrar
    ],alignment=ft.MainAxisAlignment.CENTER))
    
ft.app(target=main)