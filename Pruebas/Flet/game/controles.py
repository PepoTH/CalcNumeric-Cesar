import flet as ft
import time as t

def main(page: ft.Page):
    print('Inicio')
    page.window_resizable = False
    page.window_width = 500
    page.window_height = 300
    page.padding = 0

    page.theme_mode = ft.ThemeMode.LIGHT

    def move(e):
        if(e.key == 'Arrow Left' and jugador.x >= 10):
                jugador.x -= 20
        elif(e.key == 'Arrow Right' and jugador.x <= page.window_width-40):
            jugador.x += 20
        elif(e.key == 'Arrow Up' and jugador.y >= 10):
            jugador.y -= 20
        elif(e.key == 'Arrow Down' and jugador.y <= page.window_height-80):
            jugador.y += 20

        if(e.key == 'A' and jugador2.x >= 10):
                jugador2.x -= 20
        elif(e.key == 'D' and jugador2.x <= page.window_width-40):
            jugador2.x += 20
        elif(e.key == 'W' and jugador2.y >= 10):
            jugador2.y -= 20
        elif(e.key == 'S' and jugador2.y <= page.window_height-80):
            jugador2.y += 20

        page.update()

    jugador = ft.canvas.Rect(10,page.window_height-100,30,50,border_radius=30,
                             paint=ft.Paint(color='blue'))
    jugador2 = ft.canvas.Rect(page.window_width-40,page.window_height-100,30
                              ,50,border_radius=30,paint=ft.Paint(color='red'))
    obj = ft.canvas.Circle(10,10,10)

    cv = ft.canvas.Canvas([
        jugador,obj,jugador2
    ])

    page.on_keyboard_event = move

    page.add(cv)

    #Configuracion de distancia recorrida
    distancia = 5
    modeH = True
    modeV = True

    while(True):
        #Configuracion Horizontal
        if(modeH):
            if(obj.x >= 0 and obj.x <= page.window_width-20):
                obj.x += distancia
            else:
                modeH = False
        else:
            if(obj.x == 0):
                modeH = True
            else:
                obj.x -= distancia

        if(modeV):
            if(obj.y >= 0 and obj.y <= page.window_height-35):
                obj.y += distancia
            else:
                modeV = False
        else:
            if(obj.y == 0):
                modeV = True
            else:
                obj.y -= distancia
        
        t.sleep(0.01)

        if((obj.x >= jugador.x and obj.x <= jugador.x + jugador.width)and(obj.y >= jugador.y and obj.y <= jugador.y + jugador.height)):
            modeV = not modeV
            modeH = not modeH

        if((obj.x >= jugador2.x and obj.x <= jugador2.x + jugador2.width)and(obj.y >= jugador2.y and obj.y <= jugador2.y + jugador2.height)):
            modeV = not modeV
            modeH = not modeH
        page.update()

ft.app(target=main)