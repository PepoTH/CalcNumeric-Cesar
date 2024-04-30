import flet as ft

def main(page: ft.Page):
        
    
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 300
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_center()

    def decimal(e):
        if(txt.value != ""):
            result.value = str(int(txt.value,2))
            result.update()

    def binario(e):
        if(txt.value != ""):
            n = int(txt.value)
            lista = []
            while(n > 0):
                lista.append(str(n % 2))
                n = n // 2

            string = lista[::-1]
            result.value = ''.join(string)
            result.update()

    txt = ft.TextField(label="Binario/Decimal")
    result = ft.TextField(disabled=True)

    page.add(ft.Container(ft.Column([
        txt,ft.ElevatedButton("Binario-Decimal",on_click=decimal),
        ft.ElevatedButton("Decimal-Binario",on_click=binario),result
    ])))
    
ft.app(target=main)