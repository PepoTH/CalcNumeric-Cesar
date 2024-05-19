import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 500
    page.window_height = 300
    page.padding = 0

    page.theme_mode = ft.ThemeMode.LIGHT

    def move(e):
        if(e.key == 'Arrow Left' and jugador.x >= 10):
                jugador.x -= 10
        elif(e.key == 'Arrow Right' and jugador.x <= page.window_width-40):
            jugador.x += 10
        elif(e.key == 'Arrow Up' and jugador.y >= 10):
            jugador.y -= 10
        elif(e.key == 'Arrow Down' and jugador.y <= page.window_height-80):
            jugador.y += 10

        page.update()

    jugador = ft.canvas.Rect(page.window_width/2,page.window_height-70,30,50)

    cv = ft.canvas.Canvas([
        jugador
    ])

    page.on_keyboard_event = move

    page.add(cv)
    
ft.app(target=main)