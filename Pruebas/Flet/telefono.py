import flet as ft

def main(page: ft.Page):

    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = 'transparent'

    #Telefono en general
    
    _main_ = ft.Container(
        width=290,
        height=600,bgcolor=ft.colors.WHITE,
        border_radius=30,
        border=ft.border.all(4,'black')
        ,content=ft.Row([
            ft.Container(width=100,height=30,bgcolor='black',border_radius=30,
                        margin=10),
            ft.Row([ft.Text('hi')])
            
        ],vertical_alignment=ft.CrossAxisAlignment.START
        ,alignment=ft.MainAxisAlignment.CENTER)
        
    )
        

    page.add(_main_)
    
ft.app(target=main)