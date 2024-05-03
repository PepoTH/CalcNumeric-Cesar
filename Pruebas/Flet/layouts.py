import flet as ft

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    content1 = ft.Container(
        width=page.window_width*0.8,
        height=page.window_height*0.10,
        bgcolor='#E7E7E7',
        border_radius=30
    )
    content2 = ft.Container(
        width=page.window_width*0.8,
        height=page.window_height*0.5,
        bgcolor='#E7E7E7',
        border_radius=30
    )
    content3 = ft.Container(
        width=page.window_width*0.8,
        height=page.window_height*0.20,
        bgcolor='#E7E7E7',
        border_radius=30
    )

    page.padding = 30

    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.add(content1,content2,content3)

    def resize(e):
        content1.width = page.window_width*0.8
        content1.update()

        content2.width = page.window_width*0.8
        content2.update()

        content3.width = page.window_width*0.8
        content3.update()

    page.on_resize = resize


    #Con flet run archivo.py -r lo corres al mismo tiempo
    
ft.app(target=main)