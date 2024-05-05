import flet as ft

def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 300
    page.window_height = 350
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_center()

    page.theme_mode = ft.ThemeMode.LIGHT

    result = ft.TextField()
    area = ft.TextField()

    page.add(ft.Container(
        ft.Column([
            ft.Text('Calculo de Matrices',font_family='Poppins')
            ,area
        ],alignment=ft.MainAxisAlignment.CENTER)
    ),
        ft.Container(
            ft.Row([
                ft.ElevatedButton('Resolver',width=100),
                ft.ElevatedButton('Modificar',width=100),
                ft.IconButton(ft.icons.DELETE)
            ],spacing=2)
        ),result)
    
ft.app(target=main)