import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 300
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.window_center()

    page.theme_mode = ft.ThemeMode.LIGHT

    def formato():

        f = """
    c1x1 + c2x2 ... cNxN
    ....
    cNxN + cNxN ... cNxN
            """

        return f

    page.add(ft.TextField(multiline=True,min_lines=5
                          ,hint_text=formato(),content_padding=10))
    
ft.app(target=main)