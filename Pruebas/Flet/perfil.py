import flet as ft

def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 300
    page.window_height = 500
    page.padding = 15

    page.theme_mode = 'light'

    titulo = ft.Container(ft.Row([
        #Foto Instagram - Logo
        ft.Image('/Users/cesar/Downloads/instagram.png'),
        ft.Text('Perfil',font_family='Poppins',weight=ft.FontWeight.W_600)
        ],alignment=ft.MainAxisAlignment.START,spacing=75
    ),width=page.window_width*0.9,height=page.height*0.15/2
    )

    foto = ft.Row([
        #Foto Persona
        ft.Image('/Users/cesar/Desktop/Semestre/Estudiantes/pngtree-young-professional-asian-college-man-with-glasses-image_2550347.jpg',
                    width=150,height=150,fit=ft.ImageFit.COVER,border_radius=100)]
                    ,alignment=ft.MainAxisAlignment.CENTER)
    
    publicaciones = ft.Container(
        ft.Column([
            ft.Row([
                ft.Container(bgcolor='black12',width=75,height=75,border_radius=10),
                ft.Container(bgcolor='black12',width=75,height=75,border_radius=10),
                ft.Container(bgcolor='black12',width=75,height=75,border_radius=10)
            ]),
            ft.Row([
                ft.Container(bgcolor='black12',width=75,height=75,border_radius=10),
                ft.Container(bgcolor='black12',width=75,height=75,border_radius=10),
                ft.Container(bgcolor='black12',width=75,height=75,border_radius=10)
            ]),

        ]),padding=10
        )
    
    crear = ft.Row([
        ft.IconButton(ft.icons.HOME,icon_color='black')

        ,ft.IconButton(ft.icons.ADD,icon_color='blue'),
        ft.IconButton(ft.icons.FAVORITE,icon_color='red')
    ],width=page.window_width*0.9,alignment=ft.MainAxisAlignment.CENTER)

    page.add(titulo,foto,publicaciones,crear)
    
ft.app(target=main)