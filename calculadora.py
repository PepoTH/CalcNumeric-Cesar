import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 400

    #Cambiando el tema
    page.theme_mode = ft.ThemeMode.DARK

    txt = ft.TextField(disabled=True,value="0",text_align="right")
    page.add(txt)

    def click(e):
        txt.value = button.text
    

    for i in range(1,10,3):
        page.add(ft.Row([
            ft.ElevatedButton(f"{i}",width=85,height=50,on_click=click),
            ft.ElevatedButton(f"{i + 1}",width=85,height=50,on_click=click),
            ft.ElevatedButton(f"{i + 2}",width=85,height=50,on_click=click)
        ]))
     


    
    
ft.app(target=main)