import flet as ft
import time as t

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 500
    page.window_height = 300

    page.theme_mode = ft.ThemeMode.LIGHT

    obj = ft.canvas.Circle(10,10,20,ft.Paint('#252525'))

    canvas = ft.canvas.Canvas(
        [obj]
    )
    page.add(canvas)
    mode = True
    vertical = True

    while(True):

        if(obj.x == page.window_width - 30):
            mode = False
        if(obj.x == 10):
            mode = True

        if(mode):
            obj.x += 10
        else:
            obj.x -= 10

        if(obj.y == page.window_height - 40):
            vertical = False
        if(obj.y == 10):
            vertical = True

        if(vertical):
            obj.y += 10
        else:
            obj.y -= 10

        
        t.sleep(0.03)
        page.update()
    
    
ft.app(target=main)